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
