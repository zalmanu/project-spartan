# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0002_offer_post'),
        ('spartans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='spartan',
            field=models.ForeignKey(related_name='bids', to='spartans.Spartan'),
        ),
    ]
