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

import uuid

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

from posts.models import Announcement


class Room(models.Model):
    spartan = models.ForeignKey(User, related_name='spa_rooms')
    employer = models.ForeignKey(User, related_name='empl_rooms')
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    post = models.OneToOneField(Announcement, primary_key=True, default='')

    def get_absolute_url(self):
        return reverse('room', args=[self.slug])


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    message = models.CharField(max_length=999)
    submitter = models.ForeignKey(User, related_name='messages', default='')
    timestamp = models.DateTimeField(editable=False,
                                     auto_now_add=True, null=True)

