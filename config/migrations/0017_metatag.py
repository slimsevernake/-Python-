# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-12 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0016_siteconfig_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='[title]', max_length=250, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('title_meta', models.CharField(default='[title]', max_length=250, verbose_name='Meta title')),
                ('description_meta', models.TextField(default='[title]', verbose_name='Meta description')),
                ('h1', models.CharField(default='[title]', max_length=250, verbose_name='H1 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('type', models.CharField(choices=[('MP', '\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430'), ('SC', '\u0420\u0430\u0437\u0434\u0435\u043b'), ('SS', '\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b'), ('CA', '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'), ('BR', '\u0411\u0440\u0435\u043d\u0434'), ('BF', '\u0411\u0440\u0435\u043d\u0434 + \u0444\u0438\u043b\u044c\u0442\u0440'), ('PD', '\u0422\u043e\u0432\u0430\u0440')], max_length=2, unique=True, verbose_name='\u0422\u0438\u043f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0442\u0430 \u0442\u0435\u0433',
                'verbose_name_plural': '\u041c\u0435\u0442\u0430 \u0442\u0435\u0433\u0438',
            },
        ),
    ]