# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
from django import forms
from django.utils.translation import ugettext_lazy as _

from shop.catalogue.models import AttributeOptionGroup, ProductAttribute
from shop.catalogue.widgets import CustomFilterCheckboxSelectMultiple
from shop.catalogue.fields import CustomFilterMultipleChoiceField
from shop.catalogue.fields import NonValidationMultipleChoiceField
from shop.catalogue.search_handlers import SolrProductSearchHandler


class FilterForm(forms.Form):
    attr_fields = {
        ProductAttribute.INTEGER: forms.IntegerField,
        ProductAttribute.FLOAT: forms.FloatField,
    }

    def __init__(self, site, categories, request, *args, **kwargs):
        self.site = site
        self.categories = categories
        self.request = request
        super(FilterForm, self).__init__(*args, **kwargs)
        self.make_filter()

    def make_filter(self):
        for attr in ProductAttribute.objects.filter(
                product_class__site=self.site, type__in=self.attr_fields):
            code = 'filter_%s' % attr.code
            values = list(attr.productattributevalue_set.values_list(
                'value_%s' % attr.type, flat=True))
            values.sort()
            first = values[0]
            number = int(math.ceil((values[-1] - values[0]) / 5.0))
            choices = []
            for i in range(5):
                choices.append(
                    [first if i == 0 else first + 1, first + number])
                first = first + number

            self.fields[code] = NonValidationMultipleChoiceField(
                widget=CustomFilterCheckboxSelectMultiple(),
                label=attr.name,
                required=False,
                choices=[(
                    '%s,%s' % (i[0], i[1]),
                    '%s - %s' % (i[0], i[1]),
                    {
                        'product_count': self.product_count(attr.code, i),
                        'attrs': {'data-min': i[0], 'data-max': i[1]},
                    }
                )for i in choices],
            )

        for group in AttributeOptionGroup.objects.filter(site=self.site):
            code = group.get_filter_param()
            self.fields[code] = \
                CustomFilterMultipleChoiceField(
                    widget=CustomFilterCheckboxSelectMultiple(),
                    label=group.name,
                    required=False,
                    choices=[(
                        i.id,
                        i.option,
                        {
                            'product_count': self.product_count_group(code, i),
                            'attrs': {},
                        }
                    )for i in group.options.all()],
            )

    def query(self, without=None):
        full_path = self.request.get_full_path()
        if int(self.request.GET.get('page', 0)) == 1:
            path_to_request = full_path.split('?')[0]
        else:
            path_to_request = full_path
        options = dict(self.data)
        if without and options.get(without):
            del options[without]
        handler = SolrProductSearchHandler(
            self.request.GET, path_to_request, self.request,
            options=options, categories=self.categories)
        return handler.get_search_queryset()

    def product_count(self, code, option):
        sqs = self.query(without='filter_%s' % code)
        values = range(int(option[0]), int(option[1]) + 1)
        sqs = sqs.filter(
            attribute_codes=code,
            attribute_values__in=values,
        )
        return sqs.count()

    def product_count_group(self, code, option):
        sqs = self.query(without=code)
        sqs = sqs.filter(
            attribute_option_values__in=[option.id],
        )
        return sqs.count()

    def get_form_selected(self):
        data = self.cleaned_data
        result = {}
        for data_item in data:
            field = self.fields[data_item]
            for selected in data[data_item]:
                for choice in field.choices:
                    if str(choice[0]) == str(selected):
                        if result.get(field.label) is None:
                            result[field.label] = []
                        result[field.label].append(choice[1])
        price_range_min = self.request.GET.get('price_range_min')
        price_range_max = self.request.GET.get('price_range_max')
        if price_range_min or price_range_max:
            result[_(u'Цена')] = ['{0} - {1}'.format(
                price_range_min, price_range_max)]
        return result
