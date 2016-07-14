# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_announcement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='announcement',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(height_field='height_field ', width_field='width_field', null=True, upload_to=b'', blank=True),
        ),
    ]
