# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20160718_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 7, 18, 14, 14, 24, 417564, tzinfo=utc), null=True, verbose_name='Review publication day'),
        ),
    ]
