# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20160714_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 7, 15, 8, 25, 59, 387112, tzinfo=utc), null=True, verbose_name='Review publication day'),
        ),
    ]
