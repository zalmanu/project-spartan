# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=1000, null=True, verbose_name='Review message')),
                ('data', models.DateField(default=datetime.datetime(2016, 7, 17, 18, 18, 25, 162173, tzinfo=utc), null=True, verbose_name='Review publication day')),
            ],
        ),
        migrations.CreateModel(
            name='UrlUnique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('un_hash', models.CharField(unique=True, max_length=33, verbose_name='Url')),
                ('expired', models.BooleanField(default=False)),
            ],
        ),
    ]
