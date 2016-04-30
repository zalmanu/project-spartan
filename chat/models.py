from __future__ import unicode_literals

import uuid
import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

from authentication.models import Spartan
from bidding.models import Oferta
from useractions.models import Announcement 


class Room(models.Model):
    spartan = models.ForeignKey(User, related_name='spa_rooms')
    employer = models.ForeignKey(User, related_name='empl_rooms')
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    post = models.OneToOneField(Announcement, primary_key=True, default='')

    def get_absolute_url(self):
        return reverse('room', args=[self.slug])

    
class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    message = models.TextField()
    submitter = models.ForeignKey(User, related_name='messages', default='')
    timestamp = models.DateTimeField(editable=False, auto_now_add=True, null=True)
