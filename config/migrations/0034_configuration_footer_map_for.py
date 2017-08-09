# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-07 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0033_configuration_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='footer_map_for',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer_map', to='contacts.City', verbose_name='\u041a\u0430\u0440\u0442\u0430 \u0432 \u0444\u0443\u0442\u0435\u0440\u0435 \u0434\u043b\u044f'),
        ),
    ]
