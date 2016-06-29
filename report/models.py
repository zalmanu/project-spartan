from __future__ import unicode_literals
from djago import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.db import models


class Report(models.Model):
    username = models.CharField(null=True, max_length=20)
    status = models.CharField(null=True, max_length=20)
    author = models.ForeignKey(to=User, related_name='reports',
                               null=True, blank=True)
    text = models.CharField(null=True, max_length=5000)


class CreateReportForm(forms.ModelForms):

    class Meta:
        model = Report
        fields = '_all_'

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateReportForm, self).__init__(*args, **kwargs)

    def clean_status(self):
        username = self.cleaned_data['username']
        status = self.cleaned_data['status']
        try:
            user = User.objects.get(username=username)
            if self.user.username == username:
                raise ValidationError("You can't report yourself!")
            elif status == "Spartan" and not user.account.has_related_object:
                raise ValidationError("This user is not a spartan")
        except User.DoesNotExist:
            raise ValidationError("This user does not exists")
