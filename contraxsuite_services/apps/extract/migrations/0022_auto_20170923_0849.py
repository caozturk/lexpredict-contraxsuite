# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extract', '0021_auto_20170923_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datedurationusage',
            name='duration',
        ),
        migrations.AddField(
            model_name='datedurationusage',
            name='duration_days',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datedurationusage',
            name='amount_str',
            field=models.CharField(blank=True, db_index=True, max_length=150, null=True),
        ),
    ]
