# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-19 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0046_auto_20171019_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='undercat_block_url_ua',
            field=models.CharField(blank=True, max_length=128, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043f\u043e\u0434 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u043e\u043c_ua'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='undercat_block_url',
            field=models.CharField(blank=True, max_length=128, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043f\u043e\u0434 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u043e\u043c_ru'),
        ),
    ]