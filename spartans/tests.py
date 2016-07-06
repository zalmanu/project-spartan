from django.test import TestCase
from django.contrib.auth.models import User

from spartans.models import Spartan
from categories.models import Category
from .models import CreateSpartanForm
from authentication.models import Account


class SpartanFormsTestCase(TestCase):
    def setUp(self):
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
        self.category = Category.objects.create(name="TestCategory",
                                                path_bg="test",
                                                path_banner="test",
                                                path_icon="tes",
                                                path_mini="test")
        self.category.save()
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

    def test_invalid_spartan_form(self):
        form_data = {'last_name': 'Gheorge',
                     'first_name': 'CelFrumos', 'birthday': '2013',
                     'address': 'Lestrada', 'cnp': '&&&',
                     'series': 'Dwda', 'cui': 'dawda', 'bank': '32'}
        form = CreateSpartanForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())

    def test_user_is_already_spartan(self):
        form_data = {'last_name': 'Gheorge',
                     'first_name': 'CelFrumos', 'birthday': '2013-02-13',
                     'address': 'Lestrada', 'cnp': '12313',
                     'series': 'Dwda', 'cui': 'dawda',
                     'category': self.category.name,
                     'bank': '1234123412341234'}
        form = CreateSpartanForm(data=form_data, user=self.spartan)
        self.assertFalse(form.is_valid())

    def tests_user_is_not_spartan(self):
        form_data = {'last_name': 'Gheorge',
                     'first_name': 'CelFrumos', 'birthday': '2013-03-12',
                     'address': 'Lestrada', 'cnp': '1231d3',
                     'series': 'Dwda', 'cui': 'dawda',
                     'category': self.category.name,
                     'bank': '1234123412341234'}
        form = CreateSpartanForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())
