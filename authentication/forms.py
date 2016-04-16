from django import forms 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(), label='Password')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    email = forms.CharField(max_length=100, label='Email', widget=forms.EmailInput())
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=100, label='Retype password', widget=forms.PasswordInput())
    country = forms.CharField(max_length=100, label='Country')
    city = forms.CharField(max_length=100, label='City')
    phone = forms.IntegerField(label='Phone number')

