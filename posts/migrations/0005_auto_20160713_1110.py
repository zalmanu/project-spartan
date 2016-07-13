# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20160713_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='image2',
            field=models.ImageField(height_field='height_field', width_field='width_field', null=True, upload_to=posts.models.upload_location, blank=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='image3',
            field=models.ImageField(height_field='height_field', width_field='width_field', null=True, upload_to=posts.models.upload_location, blank=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='image4',
            field=models.ImageField(height_field='height_field', width_field='width_field', null=True, upload_to=posts.models.upload_location, blank=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(height_field='height_field', width_field='width_field', null=True, upload_to=posts.models.upload_location, blank=True),
        ),
    ]
