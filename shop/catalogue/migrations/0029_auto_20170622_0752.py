# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-22 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0028_auto_20170622_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='filterdescription',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='filterdescription',
            name='description_uk',
            field=models.TextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='filterdescription',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AddField(
            model_name='filterdescription',
            name='title_uk',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]