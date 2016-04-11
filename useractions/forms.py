from django import forms 

class ProfileEditForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    telefon = forms.IntegerField(max_length=100)
    
