from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.urlresolvers import reverse
from authentication.models import Spartan
from categories.models import Category


class Announcement(models.Model):
    title = models.CharField(null=True, max_length=20)
    text = models.CharField(null=True, max_length=500)
    slug = models.SlugField(default=uuid.uuid1, unique=True)
    author = models.ForeignKey(to=User, related_name='posts',
                               null=True, blank=True)
    address = models.CharField(null=True, max_length=500)
    country = models.TextField(null=True, max_length=50)
    city = models.TextField(null=True, max_length=100)
    data = models.DateField('Task-ul trebuie indeplinit in data de',
                            null=True)
    creation_date = models.DateTimeField(editable=False, auto_now_add=True,
                                         null=True)
    timePost = models.TimeField('Ora', null=True)
    category = models.ForeignKey(Category, null=True)
    money = models.IntegerField(null=True)
    spartan = models.ForeignKey(Spartan, related_name='anunturi', null=True,
                                blank=True)
    pret = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default = False)
    employer_done = models.BooleanField(default = False)
    spartan_done = models.BooleanField(default = False)
    
    def get_absolute_url(self):
        return reverse('post', args=[self.slug])

    class Meta:
        get_latest_by = 'creation_date'
