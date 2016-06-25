from django import forms
from categories.models import Category


class SpartanForm(forms.Form):
    first_name = forms.CharField(max_length=40, label="First name",
                                 widget=forms.TextInput(
                                  attrs={'required': 'required'}))
    last_name = forms.CharField(max_length=40, label="Last name",
                                widget=forms.TextInput(
                                    attrs={'required': 'required'}))
    birthday = forms.DateField(label="Bitrthday", widget=forms.TextInput(
        attrs={'class': "form-control event_input tcal",
               'required': 'required'}))
    adress = forms.CharField(max_length=500, label="Adress",
                             widget=forms.TextInput(
                                 attrs={'required': 'required'}))
    CNP = forms.IntegerField(label="CNP", widget=forms.NumberInput(
        attrs={'required': 'required'}))
    series = forms.CharField(max_length=30, label="ID card series",
                             widget=forms.TextInput(
                                 attrs={'required': 'required'}))
    cui = forms.CharField(max_length=30, label="CUI",
                          widget=forms.NumberInput(
                              attrs={'required': 'required'}))
    bank_account = forms.CharField(max_length=30, label="Banck account",
                                   widget=forms.NumberInput(
                                       attrs={'required': 'required'}))
    category = forms.ChoiceField(choices=[(x, x)
                                          for x in Category.categories()],
                                 label="Category", widget=forms.Select(
            attrs={'class': "form-control input-lg m-bot15",
                   'id': "choose_category", 'required': 'required'}))
