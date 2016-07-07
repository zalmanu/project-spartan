from __future__ import unicode_literals

from django.db import models

from spartans.models import Spartan
from posts.models import Announcement


class Offer(models.Model):
    price = models.IntegerField(null=True)
    spartan = models.ForeignKey(Spartan, related_name='bids')
    post = models.ForeignKey(Announcement, related_name='offers')
    kind = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

