# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='id_hash',
            field=models.CharField(default=b'', max_length=10000),
        ),
    ]
