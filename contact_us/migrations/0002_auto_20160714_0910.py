# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='name',
        ),
        migrations.AddField(
            model_name='contactus',
            name='first_name',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='contactus',
            name='last_name',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
