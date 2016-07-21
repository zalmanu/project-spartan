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

from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User

from .models import Announcement
from .views import post, edit_post


class PostsViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester",
                                             email="smt@smt.com",
                                             password="top_secret")
        self.user.save()
        self.user2 = User.objects.create_user(username="testerspartan",
                                              email="smt@gmail.com",
                                              password="top_secret2")
        self.user2.save()
        self.post = Announcement.objects.create(title="Zugrav",
                                                description="Asa de un zugrav",
                                                author=self.user,
                                                price=200)
        self.post.save()

    def test_delete_post_from_another_user(self):
        request = self.factory.post(self.post.get_absolute_url(),
                                    {'deletePost': 'what'})
        request.user = self.user2
        title = self.post.title
        post(request, self.post.slug)
        self.assertTrue(Announcement.objects.filter(title=title).count())

    def test_invalid_user_edit_post(self):
        request = self.factory.post('/edit')
        request.user = self.user2
        resposne = edit_post(request, self.post.slug)
        self.assertNotEqual(resposne.status_code, 200)

    def test_search_empty_data(self):
        request = self.client.get('/search/')
        request.user = self.user
        self.assertIsNone(request.context)

    def test_search_valid_data(self):
        request = self.client.get('/search/', {'q': 'Zugrav'})
        request.user = self.user
        print request.response
        self.assertTrue(request.response)
