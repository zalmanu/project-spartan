# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-06 07:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_auto_20160706_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 7, 6, 7, 29, 49, 182935, tzinfo=utc), null=True, verbose_name='Review publication day'),
        ),
    ]
