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

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from authentication.models import Account
from spartans.models import Spartan
from .forms import CreateReportForm


class ReportFormTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester",
                                             email="smt@smt.com",
                                             password="top_secret")
        self.spartan = User.objects.create_user(username="testerspartan",
                                                email="smt@gmail.com",
                                                password="top_secret2")
        account = Account.objects.create(city="Timisoara", country="Romania",
                                         user=self.user)
        account.save()
        accountspar = Account.objects.create(city="Timisoara",
                                             country="Romania",
                                             user=self.spartan)
        accountspar.save()
        spartan = Spartan.objects.create(last_name="Males",
                                         first_name="Sebastian",
                                         birthday="2014-03-12",
                                         address="La mine acas",
                                         cnp="dawd2",
                                         series="dawdaw",
                                         cui="dwda",
                                         bank="1234123412341234",
                                         user=self.spartan,
                                         spartanStatus=True)
        spartan.save()

    def test_invalid_employer(self):
        form_data = {'username': 'Blablbab', 'status': 'Employer',
                     'author': self.user, 'text': 'Whaaaaat'}
        form = CreateReportForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())

    def test_invalid_user_as_spartan(self):
        form_data = {'username': 'Blablbab', 'status': 'Spartan',
                     'author': self.user, 'text': 'Whaaaaat'}
        form = CreateReportForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())

    def test_invalid_spartan(self):
        form_data = {'username': 'testerspart', 'status': 'Spartan',
                     'author': self.user, 'text': 'Whaaaaat'}
        form = CreateReportForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())

    def test_employer_is_me(self):
        form_data = {'username': self.user.username, 'status': 'Spartan',
                     'author': self.user, 'text': 'Whaaaaat'}
        form = CreateReportForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())

    def test_valid_spartan(self):
        form_data = {'username': 'testerspartan', 'status': 'Spartan',
                     'author': self.user, 'text': 'Whaaaaat'}
        form = CreateReportForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_valid_employer(self):
        form_data = {'username': 'testerspartan', 'status': 'Employer',
                     'author': self.user, 'text': 'Whaaaaat'}
        form = CreateReportForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())
