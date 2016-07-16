# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_notification_id_hash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='html',
        ),
    ]
