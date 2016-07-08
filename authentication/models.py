from __future__ import unicode_literals
import md5

from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from spartans.models import Spartan


class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=36, null=True)
    phone = PhoneNumberField(null=True)
    code = models.CharField(max_length=100, null=True, blank=True)

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

