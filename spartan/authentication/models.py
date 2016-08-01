# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from spartans.models import Spartan


def upload_location(instance, filename):
    return "%s/%s" % (instance.user, filename)


class Country(models.Model):
    name = models.CharField(max_length=36, null=True)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='cities')

    def __unicode__(self):
        return self.name


class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    city = models.ForeignKey(City, related_name='accounts', default='')
    country = models.ForeignKey(Country, related_name='accounts', default='')
    phone = PhoneNumberField(null=True)
    profile_image = models.ImageField(upload_to=upload_location,
                                      null=True, blank=True)

    def has_related_object(self):
        has_spartan = False
        try:
            has_spartan = (self.user.spartan is not None)
        except Spartan.DoesNotExist:
            pass
        return has_spartan and (self.user is not None)
