from __future__ import unicode_literals

from django.db import models
from authentication.models import Spartan,User
from useractions.models import Announcement


# Create your models here.


class Review(models.Model):
    review = models.OneToOneField(Announcement, primary_key=True,default=None)
    receiver = models.ForeignKey(Spartan, related_name='reviews')
    submitter = models.ForeignKey(User, related_name='reviews')
    message=models.CharField(null=True, max_length=1000)
    data=models.DateField('Data publicarii review-ului', null=True)
    creation_date = models.DateTimeField(editable=False, auto_now_add=True, null=True)