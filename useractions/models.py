from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.urlresolvers import reverse


class Announcement(models.Model):
    title = models.CharField(null=True, max_length=20)
    text = models.CharField(null=True, max_length=500)
    slug = models.SlugField(default=uuid.uuid1, unique=True)
    author = models.ForeignKey(User, null=True, blank=True)
    address = models.CharField(null=True, max_length=500)
    country = models.TextField(null=True, max_length=50)
    city = models.TextField(null=True, max_length=100)
    data = models.DateField('Task-ul trebuie indeplinit in data de', null=True)
    creation_date = models.DateTimeField(editable=False, auto_now_add=True, null=True)
    timePost = models.TimeField('Ora', null=True)
    category = models.CharField(null=True, max_length=20)
    
    def get_absolute_url(self):
        return reverse('announcement', args=[self.slug])
    
    class Meta:
        get_latest_by = 'creation_date'
