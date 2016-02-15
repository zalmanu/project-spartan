from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    city = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    photo = models.ImageField(null=True)
    descriere = models.TextField(max_length=300, null=True)