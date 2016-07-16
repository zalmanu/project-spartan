# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_remove_notification_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='html',
            field=models.CharField(max_length=90000, blank=True),
        ),
    ]
