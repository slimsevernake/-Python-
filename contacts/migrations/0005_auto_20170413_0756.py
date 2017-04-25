# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_socialnetref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialnetref',
            name='ref_type',
            field=models.CharField(choices=[('facebook', 'facebook'), ('vkontakte', '\u0412\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u0435'), ('mailru', 'mail.ru'), ('twitter', 'Twitter'), ('odnoklassniki', '\u041e\u0434\u043d\u043e\u043a\u043b\u0430\u0441\u0441\u043d\u0438\u043a\u0438'), ('pinterest', 'Pinterest'), ('google', 'Google+'), ('youtube', 'YouTube')], default='facebook', max_length=20, verbose_name='\u041e\u043f\u0435\u0440\u0430\u0442\u043e\u0440'),
        ),
    ]