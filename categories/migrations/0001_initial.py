# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True)),
                ('path_banner', models.CharField(max_length=500, null=True)),
                ('path_bg', models.CharField(max_length=500, null=True)),
                ('path_icon', models.CharField(max_length=500, null=True)),
                ('path_mini', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
