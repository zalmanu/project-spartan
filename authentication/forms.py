from captcha.fields import ReCaptchaField
from django.contrib.auth.models import User
from django import forms
from .models import Account


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username',
                               widget=forms.TextInput(attrs={
                                   'required': 'required'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'required': 'required'}),
                               label='Password')


class PasswordResetForm(forms.Form):
    old_password = forms.CharField(max_length=160, min_length=8,
                                   label="Old password",
                                   widget=forms.PasswordInput(
                                  attrs={'required': 'required'}))
    password_1 = forms.CharField(max_length=160, min_length=8, label="New password",
                                 widget=forms.PasswordInput(
                                attrs={'required': 'required'}))
    password_2 = forms.CharField(max_length=160, min_length=8,
                                 label="Type again the new password",
                                 widget=forms.PasswordInput(
                                attrs={'required': 'required'}))


class ForGotPassword(forms.Form):
    password_1 = forms.CharField(max_length=160, min_length=8, label="New password",
                                 widget=forms.PasswordInput(
                                attrs={'required': 'required'}))
    password_2 = forms.CharField(max_length=160, min_length=8,
                                 label="Type again the new password",
                                 widget=forms.PasswordInput(
                                attrs={'required': 'required'}))



class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Retype password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError("This email already exists")
        return email

    def clean_username(self):
        user_name = self.cleaned_data['username']
        if User.objects.filter(username=user_name).count():
            raise forms.ValidationError("This username already exists")
        return user_name

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password.isdigit():
            raise forms.ValidationError("Password is entirely numeric")
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        if len(password) < 8:
            raise forms.ValidationError("Password is too short")
        return password2


class AccountRegisterForm(forms.ModelForm):

    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']])
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']])
    captcha = ReCaptchaField()

    class Meta:
        model = Account
        exclude = ['user', 'code']

