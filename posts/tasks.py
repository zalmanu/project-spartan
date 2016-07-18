from __future__ import absolute_import

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from celery import task

from spartans.models import Spartan
from notifications.models import Notification
from categories.models import Category


@task
def notify_spartans(category_name, city, username, url, id_hash):
    category = Category.objects.get(name=category_name)
    for spartan in Spartan.objects.filter(spartanStatus=True,
                                          category=category,
                                          city=city):
        notification = Notification.objects.create(
            receiver=spartan.user, not_type="post", url=url,
            id_hash=id_hash)
        notification.save()


@task
def notify_bid(username, url, id_hash):
    receiver = User.objects.get(username=username)
    notification = Notification.objects.create(receiver=receiver,
                                               not_type="bid", url=url,
                                               id_hash=id_hash)
    notification.save()


@task
def email_user(email_message, email, subject):
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, email_message, from_email,
              [email], fail_silently=True)
