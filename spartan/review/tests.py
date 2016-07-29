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
import random

from django.test import TestCase, Client
from django.contrib.auth.models import User

from authentication.models import Account
from spartans.models import Spartan
from categories.models import Category
from review.models import UrlUnique


class ReviewViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'males@sebastia.com',
                                             'test')
        self.user.save()
        account = Account.objects.create(city="Timisoara", country="Romania",
                                         user=self.user)
        account.save()
        self.category = Category.objects.create(name="TestCategory",
                                                path_banner="test")
        self.category.save()
        self.spartan = Spartan.objects.create(last_name="Males",
                                              first_name="Sebastian",
                                              birthday="2014-03-12",
                                              address="La mine acas",
                                              cnp="dawd2",
                                              series="dawdaw",
                                              user=self.user,
                                              spartanStatus=True)
        self.spartan.save()
        self.uhash = random.getrandbits(32)
        url_hash = UrlUnique.objects.create(un_hash=self.uhash)
        url_hash.save()

    def test_view_with_no_user(self):
        request = self.client.get("/review/" + str(self.spartan.slug) +
                                  "/" + str(self.uhash) + "/")
        self.assertEqual(request.status_code, 302)

    def test_view_with_invalid_hash(self):
        self.client.login(username='testuser', password='test')
        self.client.post("/review/" + str(self.spartan.slug) +
                         "/" + str(self.uhash) + "/", {
                             "message": "mare om"
                         })
        hash_obj = UrlUnique.objects.get(un_hash=self.uhash)
        self.assertTrue(hash_obj.expired)

    def test_dont_post(self):
        self.client.login(username='testuser', password='test')
        request = self.client.post('/review/' + str(self.spartan.slug) +
                                   '/' + str(self.uhash) + '/', {
                                      "dontp": "stuff"
                                  })
        self.assertEqual(request.status_code, 302)
