# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_announcement_spartan'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='image',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
