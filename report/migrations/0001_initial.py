# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, null=True, verbose_name='Username')),
                ('status', models.CharField(max_length=20, null=True)),
                ('text', models.CharField(max_length=5000, null=True, verbose_name='Report description')),
                ('author', models.ForeignKey(related_name='reports', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
