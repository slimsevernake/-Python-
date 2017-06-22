# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-22 07:04
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0026_auto_20170621_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_url', models.CharField(max_length=255, verbose_name='URL')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('description', ckeditor.fields.RichTextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
            ],
        ),
    ]
