from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import md5
from django.core.urlresolvers import reverse
from spartan.models import Spartan



class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=36, null=True)
    telefon = models.CharField(null=True, max_length=20)
    cod = models.CharField(max_length=100,null=True, blank=True)

    def has_related_object(self):
        has_spartan = False
        try:
            has_spartan = (self.user.spartan is not None)
        except Spartan.DoesNotExist:
            pass
        return has_spartan and (self.user is not None)

    def gravatar_photo(self):
        usshash = md5.new()
        usshash.update(self.user.email)
        return usshash.hexdigest()
