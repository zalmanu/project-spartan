from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from .model import UserRegisterForm, AccountRegisterForm, Account


class AuthTestCase(TestCase):
    def setup(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester",
                                             email="smt@smt.com",
                                             password="top_secret")
        account = Account.objects.create_user(user=self.user,
                                              city="Timisoara",
                                              country="Romania")
        account.save()

    def test_user_form(self):
        form_data = {'username': 'tester', 'email': 'smt@smt.com',
                     'password': '1231', 'password': '23232332daw'}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
