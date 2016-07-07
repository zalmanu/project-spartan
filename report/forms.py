from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from .models import Report


class CreateReportForm(forms.ModelForm):

    status = forms.ChoiceField(choices=[(x, x) for x in ['Employer',
                                                         'Spartan']])

    class Meta:
        model = Report
        exclude = ["author"]

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
