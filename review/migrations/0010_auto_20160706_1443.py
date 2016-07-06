# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-06 14:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0009_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 7, 6, 14, 43, 59, 502887, tzinfo=utc), null=True, verbose_name='Review publication day'),
        ),
    ]