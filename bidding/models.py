from __future__ import unicode_literals

from django.db import models

from authentication.models import Spartan
from useractions.models import Announcement


class Oferta(models.Model):
    pret = models.IntegerField(null=True)
    spartan = models.ForeignKey(Spartan, related_name='spartan')
    post = models.ForeignKey(Announcement, related_name='oferte')
    tip = models.CharField(max_length=30)
