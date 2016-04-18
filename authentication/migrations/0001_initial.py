# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 13:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('city', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=30, null=True)),
                ('telefon', models.IntegerField(null=True)),
                ('cod', models.CharField(blank=True, max_length=100, null=True)),
                ('sold', models.IntegerField(default=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
                ('SpartanStatus', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
