from django.test import TestCase
from django.contrib.auth.models import User

from .models import UserRegisterForm, AccountRegisterForm
from .forms import LoginForm


class AuthFormsTestCase(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username="tester",
                                             email="smt@smt.com",
                                             password="top_secret")

    def test_valid_login_form(self):
        form_data = {'username': 'tester', 'password': 'top_seret'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_user_form(self):
        form_data = {'username': 'tester', 'email': 'smt@smt.com',
                     'password': '1231', 'password2': '23232332daw'}
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_valid_user_form(self):
        form_data = {'username': 'usernamedetest', 'email': 'sdwmt@gmail.com',
                     'password': 'aloha123', 'password2': 'aloha123'}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def tests_account_valid_phone(self):
        form_data = {'city': 'Timisoara', 'country': 'Romania',
                     'phone': '+40736180165'}
        form = AccountRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def tests_account_invalid_phone(self):
        form_data = {'city': 'Timisoara', 'country': 'Romania',
                     'phone': '+4073618'}
        form = AccountRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
