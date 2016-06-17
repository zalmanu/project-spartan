from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Report(models.Model):
    username = models.CharField(null=True, max_length=20)
    status = models.CharField(null=True, max_length=20)
    author = models.ForeignKey(to=User, related_name='reports',
                               null=True, blank=True)
    text = models.CharField(null=True, max_length=5000)
