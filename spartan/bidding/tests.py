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

from .models import Offer
from .views import posts
from authentication.models import Account
from spartans.models import Spartan
from posts.models import Announcement


class AuthFormsTestCase(TestCase):
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
                                         user=self.spartan,
                                         spartanStatus=True)
        spartan.save()
        self.post = Announcement.objects.create(title="Zugrav",
                                                description="Asa de un zugrav",
                                                author=self.user,
                                                price=200)
        self.post.save()
        self.offer = Offer.objects.create(price=20,
                                          spartan=self.spartan.spartan,
                                          post=self.post)
        self.offer.save()

    def test_offer_view(self):
        request = self.factory.post('/posts', {"offer": self.offer.id})
        request.user = self.user
        posts(request)
        off = Offer.objects.get(id=self.offer.id)
        self.assertTrue(off.status)
        request = self.factory.post('/posts', {"post": self.post.id})
        request.user = self.user
        posts(request)
        post = Announcement.objects.get(id=self.post.id)
        self.assertTrue(post.spartan_done)

    def test_invalid_post_argument(self):
        request = self.factory.post('/posts', {"dawd": "dwada"})
        request.user = self.user
        response = posts(request)
        self.assertNotEqual(response.status_code, 200)
