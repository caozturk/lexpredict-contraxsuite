# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-12 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0090_auto_20181009_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenttype',
            name='editor_type',
            field=models.CharField(blank=True, choices=[('save_by_field', 'save_by_field'), ('save_all_fields_at_once', 'save_all_fields_at_once'), ('no_text', 'no_text')], max_length=100, null=True),
        ),
    ]