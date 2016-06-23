from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from categories.models import Category


def categories():
    categories = []
    for x in Category.objects.all():
        categories.append(x.name)
    return categories


class PostForm(forms.Form):
    title = forms.CharField(max_length=256, label="Title",
                            widget=forms.TextInput(
                                attrs={'required': 'required'}))
    text = forms.CharField(max_length=500, label="Announcement description",
                           widget=forms.TextInput(
                               attrs={'required': 'required'}))
    adress = forms.CharField(max_length=500, label="Adress",
                             widget=forms.TextInput(
                                 attrs={'required': 'required'}))
    category = forms.ChoiceField(choices=[(x, x)
                                          for x in categories()],
                                 label="Category", widget=forms.Select(
                    attrs={'class': "form-control input-lg m-bot15",
                           'id': "choose_category", 'required': 'required'}))
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']],
                                label="Country", widget=forms.Select(
            attrs={'class': "form-control input-lg m-bot15",
                   'id': "choose_category", 'required': 'required'}))
    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']],
                             label="City", widget=forms.Select(
            attrs={'class': "form-control input-lg m-bot15",
                   'id': "choose_category", 'required': 'required'}))
    data = forms.DateField(label="Date", widget=forms.TextInput(
        attrs={'class': "form-control event_input tcal",
               'required': 'required'}))
    timePost = forms.CharField(label="Time", widget=forms.TextInput(
        attrs={'class': "timepicker", 'required': 'required'}))
    price = forms.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(
                                               9223372036854775807)],
                               label="Highest price you are"
                               "willing to pay (EUR)",
                               widget=forms.NumberInput(
                                   attrs={'required': 'required'}))


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
