from __future__ import unicode_literals

from django.db import models

from spartan.models import Spartan
from posts.models import Announcement


class Oferta(models.Model):
    pret = models.IntegerField(null=True)
    spartan = models.ForeignKey(Spartan, related_name='licitari')
    post = models.ForeignKey(Announcement, related_name='oferte')
    tip = models.CharField(max_length=30)
    status = models.BooleanField(default = False)

