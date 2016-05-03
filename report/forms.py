from django import forms
from captcha.fields import ReCaptchaField

class ReportForm(forms.Form):
    username= forms.CharField(max_length=20, label="Username",
                            widget=forms.TextInput(
                                attrs={'required': 'required'}))
    statut = forms.ChoiceField(choices=[(x, x)
                                          for x in
                                          ['Employer', 'Spartan', ]],
                                 label="Report", widget=forms.Select(
            attrs={'class': "form-control input-lg m-bot15",
                   'id': "choose_category", 'required': 'required'}))
    text = forms.CharField(max_length=5000, label="Report description",
                           widget=forms.TextInput(
                               attrs={'required': 'required'}))
    captcha = ReCaptchaField()