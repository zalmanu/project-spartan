from __future__ import unicode_literals

from django import forms
from django.db import models
from django.utils import timezone
from authentication.models import User
from spartans.models import Spartan


class Review(models.Model):
    receiver = models.ForeignKey(Spartan, related_name='reviews')
    submitter = models.ForeignKey(User, related_name='reviews')
    message = models.CharField("Review message", null=True, max_length=1000)
    data = models.DateField('Review publication day', null=True,
                            default=timezone.now())


class UrlUnique(models.Model):
    un_hash = models.CharField('Url', unique=True, max_length=33)
    expired = models.BooleanField(default=False)


class CreateReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['message']
