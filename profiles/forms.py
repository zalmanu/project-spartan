from django import forms


class ProfileEditForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username", required=False)
    email = forms.CharField(max_length=100, label="Email", required=False)
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']],
                                label="Country",
                                widget=forms.Select(attrs={
                                    'class': "form-control input-lg m-bot15",
                                    'id': "choose_category"}))
    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']],
                             label="City",
                             widget=forms.Select(attrs={
                                 'class': "form-control input-lg m-bot15",
                                 'id': "choose_category",
                                 'required': 'required'}))
    telefon = forms.CharField(label="Phone", required=False, max_length=20)
