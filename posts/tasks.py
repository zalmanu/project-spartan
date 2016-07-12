from __future__ import absolute_import

from celery import task

from spartans.models import Spartan
from notifications.models import Notification
from categories.models import Category


@task
def notify_spartans(category_name, city, username):
    category = Category.objects.get(name=category_name)
    for spartan in Spartan.objects.filter(spartanStatus=True,
                                          category=category):
        notification = Notification.objects.create(
            receiver=spartan.user)
        notification.spartan_notif()
        notification.save()
