# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 22:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useractions', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('post', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='useractions.Announcement')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empl_rooms', to=settings.AUTH_USER_MODEL)),
                ('spartan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spa_rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.Room'),
        ),
        migrations.AddField(
            model_name='message',
            name='submitter',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
