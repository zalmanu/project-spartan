from django import forms
from categories.models import Category


def categories():
    categories = []
    for x in Category.objects.all():
        categories.append(x.name)
    return categories


class SpartanForm(forms.Form):
    prenume = forms.CharField(max_length=40, label="First name",
                              widget=forms.TextInput(
                                  attrs={'required': 'required'}))
    nume = forms.CharField(max_length=40, label="Last name",
                           widget=forms.TextInput(
                               attrs={'required': 'required'}))
    data = forms.DateField(label="Bitrthday", widget=forms.TextInput(
        attrs={'class': "form-control event_input tcal",
               'required': 'required'}))
    adress = forms.CharField(max_length=500, label="Adress",
                             widget=forms.TextInput(
                                 attrs={'required': 'required'}))
    CNP = forms.IntegerField(label="CNP", widget=forms.NumberInput(
        attrs={'required': 'required'}))
    serie = forms.CharField(max_length=30, label="ID card series",
                            widget=forms.TextInput(
                                attrs={'required': 'required'}))
    cui = forms.CharField(max_length=30, label="CUI",
                          widget=forms.NumberInput(
                              attrs={'required': 'required'}))
    cont = forms.CharField(max_length=30, label="Banck account",
                           widget=forms.NumberInput(
                               attrs={'required': 'required'}))
    abilitate = forms.ChoiceField(choices=[(x, x)
                                           for x in categories()],
                                  label="Category", widget=forms.Select(
            attrs={'class': "form-control input-lg m-bot15",
                   'id': "choose_category", 'required': 'required'}))
