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

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

from celery import task
from channels import Group

from spartans.models import Spartan
from notifications.models import Notification
from categories.models import Category


@task
def notify_spartans(category_name, city, title, url, id_hash):
    category = Category.objects.get(name=category_name)
    for spartan in Spartan.objects.filter(spartanStatus=True,
                                          category=category):
        if spartan.user.account.city.name == city:
            notification = Notification.objects.create(
                receiver=spartan.user, not_type="post", url=url,
                id_hash=id_hash, context=title)
            notification.save()


@task
def notify_bid(username, url, title, id_hash):
    receiver = User.objects.get(username=username)
    notification = Notification.objects.create(receiver=receiver,
                                               not_type="bid", url=url,
                                               id_hash=id_hash, context=title)
    notification.save()


@task
def email_user(email_message, user, email, subject):
    from_email = settings.EMAIL_HOST_USER
    ctx = {
        'user': user,
        'email_message': email_message
    }
    to = [email]
    template = get_template('mail/mail.html').render(Context(ctx))
    mail = EmailMessage(subject, template, to=to, from_email=from_email)
    mail.content_subtype = 'html'
    mail.send()
