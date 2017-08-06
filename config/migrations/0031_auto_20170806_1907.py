# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-06 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0030_auto_20170806_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfour',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AddField(
            model_name='textfour',
            name='text_uk',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AddField(
            model_name='textone',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AddField(
            model_name='textone',
            name='text_uk',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AddField(
            model_name='textthree',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AddField(
            model_name='textthree',
            name='text_uk',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AddField(
            model_name='texttwo',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AddField(
            model_name='texttwo',
            name='text_uk',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
    ]
