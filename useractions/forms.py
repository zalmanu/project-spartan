from django import forms


class ProfileEditForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username", required=False)
    email = forms.CharField(max_length=100, label="Email", required=False)
    city = forms.CharField(max_length=100, label="City", required=False)
    country = forms.CharField(max_length=36, label="Country", required=False)
    telefon = forms.IntegerField(label="Phone", required=False)


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
    abilitate = forms.ChoiceField(choices=[(x, x) for x in
                                           ['Garden', 'Moving', 'Cleaning',
                                            'Babysitting', 'Cooking',
                                            'Others']], label="Category",
                                  widget=forms.Select(attrs={
                                      'class': "form-control input-lg m-bot15",
                                      'id': "choose_category",
                                      'required': 'required'}))
