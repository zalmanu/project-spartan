# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('bidding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='post',
            field=models.ForeignKey(related_name='offers', to='posts.Announcement'),
        ),
    ]
