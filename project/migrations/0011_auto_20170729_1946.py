# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-07-29 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20170729_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='shorText',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tool',
            name='text',
            field=models.CharField(max_length=5000),
        ),
    ]