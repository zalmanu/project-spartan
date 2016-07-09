# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('post', models.OneToOneField(primary_key=True, default='', serialize=False, to='posts.Announcement')),
                ('employer', models.ForeignKey(related_name='empl_rooms', to=settings.AUTH_USER_MODEL)),
                ('spartan', models.ForeignKey(related_name='spa_rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(related_name='messages', to='chat.Room'),
        ),
        migrations.AddField(
            model_name='message',
            name='submitter',
            field=models.ForeignKey(related_name='messages', default='', to=settings.AUTH_USER_MODEL),
        ),
    ]
