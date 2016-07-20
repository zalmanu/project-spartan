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

from __future__ import absolute_import
import string
import random

from django.contrib.auth.models import User

from celery import task

from notifications.models import Notification


@task
def notify_chat(username, url):
    id_hash = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(6))
    receiver = User.objects.get(username=username)
    notification = Notification.objects.create(receiver=receiver,
                                               not_type="chat", url=url,
                                               id_hash=id_hash)
    notification.save()
