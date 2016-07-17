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
