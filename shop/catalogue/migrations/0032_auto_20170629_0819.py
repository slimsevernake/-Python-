# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-29 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0031_populate_slugs_translations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug_ru',
            field=models.SlugField(max_length=255, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug_uk',
            field=models.SlugField(max_length=255, null=True, verbose_name='Slug'),
        ),
    ]