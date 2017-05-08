from django.contrib.sites.shortcuts import get_current_site
from django.http.response import HttpResponseRedirect
from oscar.apps.dashboard.catalogue.views import \
    ProductCreateUpdateView as OscarProductCreateUpdateView, \
    ProductClassCreateView as OscarProductClassCreateView, \
    ProductClassUpdateView as OscarProductClassUpdateView, \
    CategoryCreateView as OscarCategoryCreateView, \
    CategoryUpdateView as OscarCategoryUpdateView, \
    ProductListView as OscarProductListView, \
    CategoryListView as OscarCategoryListView, \
    ProductClassListView as OscarProductClassListView

from shop.dashboard.catalogue.forms import ProductForm, \
    ProductAttributesFormSet, ProductClassForm, CategoryForm, \
    ExtraProductImageFormSet, ProductVideoFormSet, ProductClassSelectForm
from website.views import SiteMultipleObjectMixin


class ProductCreateUpdateView(OscarProductCreateUpdateView):
    template_name = 'shop/dashboard/catalogue/product_update.html'
    form_class = ProductForm
    extra_product_image_formset = ExtraProductImageFormSet
    video_formset = ProductVideoFormSet

    def __init__(self, *args, **kwargs):
        super(ProductCreateUpdateView, self).__init__(*args, **kwargs)
        self.formsets['extra_image_formset'] = self.extra_product_image_formset
        self.formsets['video_formset'] = self.video_formset

    def clean(self, form, formsets):
        self.object.site = get_current_site(self.request)
        self.object.save()
        return super(ProductCreateUpdateView, self).clean(form, formsets)


class ProductClassCreateView(OscarProductClassCreateView):
    template_name = 'shop/dashboard/catalogue/product_class_form.html'
    product_attributes_formset = ProductAttributesFormSet
    form_class = ProductClassForm

    def forms_valid(self, form, attributes_formset):
        obj = form.save(commit=False)
        obj.site = get_current_site(self.request)
        obj.save()
        attributes_formset.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductClassUpdateView(OscarProductClassUpdateView):
    template_name = 'shop/dashboard/catalogue/product_class_form.html'
    product_attributes_formset = ProductAttributesFormSet
    form_class = ProductClassForm

    def form_valid(self, *args, **kwargs):
        self.object.site = get_current_site(self.request)
        self.object.save()
        return super(ProductClassUpdateView, self).form_valid(*args, **kwargs)


class CategoryCreateView(OscarCategoryCreateView):
    form_class = CategoryForm

    def form_valid(self, form, *args, **kwargs):
        form.cleaned_data['site'] = get_current_site(self.request)
        return super(CategoryCreateView, self).form_valid(form, *args, **kwargs)


class CategoryUpdateView(OscarCategoryUpdateView):
    form_class = CategoryForm

    def form_valid(self, *args, **kwargs):
        self.object.site = get_current_site(self.request)
        self.object.save()
        return super(CategoryUpdateView, self).form_valid(*args, **kwargs)


class ProductListView(SiteMultipleObjectMixin, OscarProductListView):
    productclass_form_class = ProductClassSelectForm
    def get_context_data(self, **kwargs):
        ctx = super(ProductListView, self).get_context_data(**kwargs)
        site = get_current_site(self.request)
        ctx['productclass_form'] = self.productclass_form_class(site=site)
        return ctx


class CategoryListView(SiteMultipleObjectMixin, OscarCategoryListView):
    pass


class ProductClassListView(SiteMultipleObjectMixin, OscarProductClassListView):
    pass


