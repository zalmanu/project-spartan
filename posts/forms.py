from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=20, label="Title",
                            widget=forms.TextInput(
                                attrs={'required': 'required'}))
    text = forms.CharField(max_length=500, label="Announcement description",
                           widget=forms.TextInput(
                               attrs={'required': 'required'}))
    adress = forms.CharField(max_length=500, label="Adress",
                             widget=forms.TextInput(
                                 attrs={'required': 'required'}))
    category = forms.ChoiceField(choices=[(x, x)
                                          for x in
                                          ['Garden', 'Moving', 'Cleaning',
                                           'Babysitting', 'Cooking',
                                           'Others']],
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
    price = forms.IntegerField(label="Highest price you are willing to pay",
                               widget=forms.NumberInput(
                                   attrs={'required': 'required'}))

class LicitatieForm(forms.Form):
    pret = forms.IntegerField(label="Liciteaza:",
                              widget=forms.TextInput(
                                  attrs={'class': "form-control",
                                         'id': "bid-input",
                                         'aria-describedby': "start-date",
                                         'required': 'required'}))
    tip = forms.ChoiceField(choices=[(x, x) for x in ['/job', '/hour']],
                            widget=forms.Select(
                                attrs={
                                    'class':
                                        "form-control input-lg m-bot15 "
                                        "bid-sort", 'id': "sort-by",
                                    'required': 'required'}))
