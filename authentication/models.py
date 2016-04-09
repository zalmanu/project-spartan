from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import md5


class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='account')
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=30, null=True)
    telefon = models.IntegerField(null=True)
    photo = models.ImageField('profile picture', upload_to="media/", null=True)
    descriere = models.CharField(max_length=244, blank=True)

    def codeimg():
        hash = md5.new()
        hash.update(user.email)
        hash.hexdigest()
        return hash.hexdigest()



class Review(models.Model):
    receiver = models.ForeignKey(User, related_name='reviews')
    submitter = models.ForeignKey(User, related_name='reviewed_by')






