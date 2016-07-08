# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_announcement_spartan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='text',
            new_name='description',
        ),
    ]
