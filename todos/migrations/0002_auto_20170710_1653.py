# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 16:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 10, 16, 53, 29, 319008)),
        ),
    ]
