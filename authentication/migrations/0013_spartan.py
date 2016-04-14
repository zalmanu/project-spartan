# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 21:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0012_remove_account_descriere'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spartan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=40)),
                ('prenume', models.CharField(max_length=40)),
                ('data_nasterii', models.DateField(null=True, verbose_name='Data nasterii')),
                ('address', models.CharField(max_length=500, null=True)),
                ('cnp', models.IntegerField(null=True)),
                ('serie', models.IntegerField(null=True)),
                ('cui', models.IntegerField(null=True)),
                ('contBancar', models.IntegerField(null=True)),
                ('abilitate1', models.CharField(max_length=20, null=True)),
                ('abilitate2', models.CharField(max_length=20, null=True)),
                ('abilitate3', models.CharField(max_length=20, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]