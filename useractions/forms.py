from django import forms 

class ProfileEditForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username:", required=False)
    email = forms.CharField(max_length=100, label="Email:", required=False)
    city = forms.CharField(max_length=100, label="City:", required=False)
    country = forms.CharField(max_length=100, label="Country:", required=False)
    telefon = forms.IntegerField(label="Phone:", required=False)


    
