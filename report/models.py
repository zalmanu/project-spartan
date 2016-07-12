from __future__ import unicode_literals
from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.db import models


class Report(models.Model):
    username = models.CharField("Username", null=True, max_length=20)
    status = models.CharField(null=True, max_length=20)
    author = models.ForeignKey(to=User, related_name='reports',
                               null=True, blank=True)
    text = models.CharField("Report description", null=True, max_length=5000)


class CreateReportForm(forms.ModelForm):

    status = forms.ChoiceField(choices=[(x, x) for x in ['Employer',
                                                         'Spartan']])
    license = forms.BooleanField()


    class Meta:
        model = Report
        exclude = ["author"]
        widgets = {'text': forms.Textarea(attrs={'required': 'required',
                                                 'placeholder': 'text'})
                   }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateReportForm, self).__init__(*args, **kwargs)


    def clean_status(self):
        username = self.cleaned_data['username']
        status = self.cleaned_data['status']
        try:
            user = User.objects.get(username=username)
            if user.username == self.user.username:
                raise ValidationError("You can't report yourself!")
            elif status == "Spartan" and not user.account.has_related_object():
                raise ValidationError("This user is not a spartan")
        except User.DoesNotExist:
            raise ValidationError("This user does not exists")
        return username
