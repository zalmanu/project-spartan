# Copyright 2015-2016 Emanuel Covaci, Fineas Silaghi, Sebastian Males
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

from spartans.models import Spartan
from posts.models import Announcement


class Offer(models.Model):
    price = models.IntegerField(null=True)
    spartan = models.ForeignKey(Spartan, related_name='bids')
    post = models.ForeignKey(Announcement, related_name='offers')
    kind = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

