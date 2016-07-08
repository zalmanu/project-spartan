# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='path_bg',
        ),
        migrations.RemoveField(
            model_name='category',
            name='path_icon',
        ),
        migrations.RemoveField(
            model_name='category',
            name='path_mini',
        ),
    ]
