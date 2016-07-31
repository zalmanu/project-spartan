# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-31 06:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location)),
                ('image2', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location)),
                ('image3', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location)),
                ('image4', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location)),
                ('description', models.CharField(max_length=500, null=True, verbose_name='Task description')),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('country', models.TextField(max_length=50, null=True)),
                ('city', models.TextField(max_length=100, null=True)),
                ('data', models.DateField(null=True, verbose_name='Date FORMAT YYYY-MM-DD')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('timePost', models.TimeField(null=True, verbose_name='Time FORMAT HH:MM:SS')),
                ('money', models.IntegerField(null=True, verbose_name='Highest price you are willing to pay (EUR)')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('employer_done', models.BooleanField(default=False)),
                ('spartan_done', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
            options={
                'get_latest_by': 'creation_date',
            },
        ),
    ]
