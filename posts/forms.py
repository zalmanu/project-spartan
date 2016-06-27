from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class BiddingForm(forms.Form):
    price = forms.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(
                                               9223372036854775807)],
                               widget=forms.TextInput(
                                  attrs={'class': "form-control",
                                         'id': "bid-input",
                                         'aria-describedby': "start-date",
                                         'required': 'required'}))
    kind = forms.ChoiceField(choices=[(x, x) for x in ['/job', '/hour']],
                             widget=forms.Select(
                                attrs={
                                    'class':
                                        "form-control input-lg m-bot15 "
                                        "bid-sort", 'id': "sort-by",
                                    'required': 'required'}))
