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
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('html', models.CharField(max_length=90000, blank=True)),
                ('not_type', models.CharField(default=b'', max_length=20)),
                ('seen', models.BooleanField(default=False)),
                ('url', models.CharField(default=b'', max_length=1000)),
                ('id_hash', models.CharField(default=b'', max_length=10000)),
                ('receiver', models.ForeignKey(related_name='notifications', default=b'', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
