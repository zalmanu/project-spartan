# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spartans', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='spartan',
            field=models.ForeignKey(related_name='anunturi', blank=True, to='spartans.Spartan', null=True),
        ),
    ]
