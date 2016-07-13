# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import authentication.models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_account_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(height_field='height_field', width_field='width_field', null=True, upload_to=authentication.models.upload_location, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
