# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 10:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_phonenumber_site'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phonenumber',
            options={'verbose_name': '\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430', 'verbose_name_plural': '\u041d\u043e\u043c\u0435\u0440\u0430 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043e\u0432'},
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c \u0432\u0432\u0435\u0434\u0435\u043d \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435:'+999999999999'. \u0414\u043e\u043f\u0443\u0441\u043a\u0430\u0435\u0442\u0441\u044f \u0434\u043e 15 \u0446\u0438\u0444\u0440 \u0432 \u043d\u043e\u043c\u0435\u0440\u0435", regex='^\\+?1?\\d{12,15}$')]),
        ),
    ]
