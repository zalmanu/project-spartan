from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import md5
from django.core.urlresolvers import reverse
from . import views


class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=30, null=True)
    telefon = models.IntegerField(null=True)
    descriere = models.CharField(max_length=244, blank=True)
    cod = models.CharField(max_length=100, null=True, blank=True)



class Review(models.Model):
    receiver = models.ForeignKey(User, related_name='reviews')
    submitter = models.ForeignKey(User, related_name='reviewed_by')







