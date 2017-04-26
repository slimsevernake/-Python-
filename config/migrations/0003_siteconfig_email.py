# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20170318_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='email',
            field=models.EmailField(default='info@defro.org.ua', max_length=254, unique=True, verbose_name='email address'),
            preserve_default=False,
        ),
    ]