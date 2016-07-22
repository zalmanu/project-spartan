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

from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    html = models.CharField(max_length=90000, blank=True)
    not_type = models.CharField(max_length=20, default='')
    seen = models.BooleanField(default=False)
    receiver = models.ForeignKey(User, related_name='notifications',
                                 default='')
    url = models.CharField(max_length=1000, default='')
    id_hash = models.CharField(max_length=10000, default='')
    context = models.CharField(max_length=10000, blank=True, default='')
