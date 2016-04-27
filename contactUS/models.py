from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ContactUS(models.Model):
    frist_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.IntegerField(null=True)
    email= models.CharField(max_length=30)
    message= models.CharField(max_length=1000, null=True)
