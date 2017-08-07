# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-07 10:26
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0035_auto_20170807_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryandpay',
            name='text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AddField(
            model_name='deliveryandpay',
            name='text_uk',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AddField(
            model_name='deliveryandpay',
            name='title_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AddField(
            model_name='deliveryandpay',
            name='title_uk',
            field=models.CharField(max_length=30, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]
