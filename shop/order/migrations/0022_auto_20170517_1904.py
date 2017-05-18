# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_order_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_placed',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.CharField(blank=True, db_index=True, max_length=128, null=True, unique=True, verbose_name=b'Order number'),
        ),
    ]
