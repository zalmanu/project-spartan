# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
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
        ('auth', '0006_require_contenttypes_0002'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spartan',
            fields=[
                ('last_name', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('birthday', models.DateField(null=True, verbose_name='Date FORMAT YYYY-MM-DD')),
                ('address', models.CharField(max_length=500, null=True)),
                ('cnp', models.CharField(max_length=20, null=True, verbose_name='CNP')),
                ('series', models.CharField(max_length=30, null=True, verbose_name='ID card series')),
                ('cui', models.CharField(max_length=30, null=True, verbose_name='CUI')),
                ('bank', models.CharField(max_length=60, null=True, verbose_name='Bank account')),
                ('user', models.OneToOneField(primary_key=True, default='', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('spartanStatus', models.BooleanField(default=False)),
                ('rating', models.IntegerField(default=0)),
                ('tasks', models.IntegerField(default=0)),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('category', models.ForeignKey(to='categories.Category', null=True)),
            ],
        ),
    ]
