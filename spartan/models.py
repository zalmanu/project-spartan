from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Spartan(models.Model):
    nume = models.CharField(max_length=40)
    prenume = models.CharField(max_length=40)
    data_nasterii = models.DateField('Data nasterii', null=True)
    address = models.CharField(null=True, max_length=500)
    cnp = models.IntegerField(null=True)
    serie = models.CharField(max_length=30, null=True)
    cui = models.CharField(max_length=30, null=True)
    contBancar = models.CharField(max_length=30, null=True)
    abilitate = models.ForeignKey(Category, null=True)
    user = models.OneToOneField(User, primary_key=True, default='')
    spartanStatus = models.BooleanField(default=False)
