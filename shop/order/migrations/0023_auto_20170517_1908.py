# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_auto_20170517_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='currency',
            field=models.CharField(default=b'UAH', max_length=12, verbose_name=b'Currency'),
        ),
        migrations.AlterField(
            model_name='order',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.Site', verbose_name=b'Site'),
        ),
    ]
