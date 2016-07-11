# Copyright 2015-2016 Emanuel Covaci, Fineas Silaghi, Sebastian Males
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
from django.http import Http404
from django.contrib.auth.models import User

from .models import Category
from .views import category
from authentication.models import Account


class CategoriesViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester",
                                             email="smt@smt.com",
                                             password="top_secret")
        account = Account.objects.create(city="Timisoara", country="Romania",
                                         user=self.user)
        account.save()
        self.category = Category.objects.create(name="TestCategory",
                                                path_bg="test",
                                                path_banner="test",
                                                path_icon="tes",
                                                path_mini="test")
        self.category.save()

    def test_valid_view(self):
        request = self.factory.get('/category')
        request.user = self.user
        status = category(request, self.category.name)
        self.assertEqual(status.status_code, 200)

    def test_invalid_view(self):
        request = self.factory.get('/category')
        request.user = self.user
        with self.assertRaises(Http404):
            category(request, "dwada")
