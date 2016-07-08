from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=120)
    seen = models.BooleanField(default=False)
