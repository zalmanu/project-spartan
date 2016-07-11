# Copyright 2015-2016 Emanuel Covaci, Fineas Silaghi, Sebastian Males
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, null=True)),
                ('text', models.CharField(max_length=500, null=True, verbose_name='Announcement description')),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('country', models.TextField(max_length=50, null=True)),
                ('city', models.TextField(max_length=100, null=True)),
                ('data', models.DateField(null=True, verbose_name='Date FORMAT YYYY-MM-DD')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('timePost', models.TimeField(null=True, verbose_name='Time FORMAT HH:MM:SS')),
                ('money', models.IntegerField(null=True, verbose_name='Highest price you are willing to pay (EUR)')),
                ('price', models.IntegerField(null=True, blank=True)),
                ('status', models.BooleanField(default=False)),
                ('employer_done', models.BooleanField(default=False)),
                ('spartan_done', models.BooleanField(default=False)),
                ('author', models.ForeignKey(related_name='posts', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('category', models.ForeignKey(to='categories.Category', null=True)),
            ],
            options={
                'get_latest_by': 'creation_date',
            },
        ),
    ]
