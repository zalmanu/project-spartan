from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=30, null=True)
    telefon = models.IntegerField(null=True)
    photo = models.ImageField('profile picture', upload_to="static/avatars", null=True, blank=True)
