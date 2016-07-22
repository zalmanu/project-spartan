# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.

from django.test import TestCase
from django.contrib.auth.models import User

from .forms import UserRegisterForm, AccountRegisterForm
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
                     'password': 'aloha123', 'retypepassword': 'aloha123'}
        form = UserRegisterForm(data=form_data)
        print form.errors
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
