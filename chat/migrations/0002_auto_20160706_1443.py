# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-06 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]