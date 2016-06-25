# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 19:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spartan',
            fields=[
                ('last_name', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('birthday', models.DateField(null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('cnp', models.IntegerField(null=True)),
                ('series', models.CharField(max_length=30, null=True)),
                ('cui', models.CharField(max_length=30, null=True)),
                ('bank_account', models.CharField(max_length=30, null=True)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('spartanStatus', models.BooleanField(default=False)),
                ('rating', models.IntegerField(default=0)),
                ('tasks', models.IntegerField(default=0)),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
        ),
    ]
