# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True)),
                ('email', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
