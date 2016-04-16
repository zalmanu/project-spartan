from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import md5
from django.core.urlresolvers import reverse
from . import views
import uuid

class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=30, null=True)
    telefon = models.IntegerField(null=True)
    cod = models.CharField(max_length=100,null=True, blank=True)
    sold= models.IntegerField(default=1000)



class Review(models.Model):
    receiver = models.ForeignKey(User, related_name='reviews')
    submitter = models.ForeignKey(User, related_name='reviewed_by')

class Spartan(models.Model):
     nume=models.CharField(max_length=40)
     prenume=models.CharField(max_length=40)
     data_nasterii=models.DateField('Data nasterii', null=True)
     address = models.CharField(null=True, max_length=500)
     cnp= models.IntegerField(null=True)
     serie = models.IntegerField(null=True)
     cui = models.IntegerField(null=True)
     contBancar = models.IntegerField(null=True)
     abilitate1= models.CharField(null=True, max_length=20)
     abilitate2= models.CharField(null=True, max_length=20)
     abilitate3= models.CharField(null=True, max_length=20)
     author = models.ForeignKey(User, null=True, blank=True)
     SpartanStatus=models.BooleanField(default=False)








