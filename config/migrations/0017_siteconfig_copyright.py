# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-12 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0016_siteconfig_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='copyright',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Copyright'),
        ),
    ]