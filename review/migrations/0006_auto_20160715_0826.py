# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_auto_20160715_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 7, 15, 8, 26, 49, 847010, tzinfo=utc), null=True, verbose_name='Review publication day'),
        ),
    ]
