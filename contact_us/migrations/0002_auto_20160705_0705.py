# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='phone',
        ),
    ]
