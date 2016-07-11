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
from django.utils import timezone
from authentication.models import User
from spartans.models import Spartan


class Review(models.Model):
    receiver = models.ForeignKey(Spartan, related_name='reviews')
    submitter = models.ForeignKey(User, related_name='reviews')
    message = models.CharField("Review message", null=True, max_length=1000)
    data = models.DateField('Review publication day', null=True,
                            default=timezone.now())


class UrlUnique(models.Model):
    un_hash = models.CharField('Url', unique=True, max_length=33)
    expired = models.BooleanField(default=False)



