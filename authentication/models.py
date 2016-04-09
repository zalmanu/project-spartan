from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import md5


class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=30, null=True)
    telefon = models.IntegerField(null=True)
    descriere = models.CharField(max_length=244, blank=True)

    @property
    def codeimg(self):
        usshash = md5.new()
        usshash.update(self.user.email)
        usshash.hexdigest()
        return usshash.hexdigest()


class Review(models.Model):
    receiver = models.ForeignKey(User, related_name='reviews')
    submitter = models.ForeignKey(User, related_name='reviewed_by')







