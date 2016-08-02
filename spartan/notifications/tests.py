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

from django.test import TestCase, Client
from django.contrib.auth.models import User

from models import Notification


class NotificationsViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'males@sebastia.com',
                                             'test')
        self.user.save()
        self.user2 = User.objects.create_user('testuser2', 'male@sebastia.com',
                                              'test')
        self.user2.save()
        self.notification = Notification.objects.create(receiver=self.user,
                                                        not_type="bid",
                                                        url="/random/",
                                                        id_hash="dwa")
        self.notification.save()

    def test_get_request(self):
        self.client.login(username='testuser', password='test')
        request = self.client.get('/seen/')
        self.assertEqual(request.status_code, 403)

    def test_view_without_notification(self):
        self.client.login(username='testuser', password='test')
        request = self.client.post('/seen/')
        self.assertEqual(request.status_code, 403)

    def test_view_no_username(self):
        request = self.client.post('/seen/',
                                   {"notif": self.notification.id_hash})
        self.assertNotEqual(request.status_code, 200)

    def test_valid_request(self):
        self.client.login(username='testuser', password='test')
        request = self.client.post('/seen/',
                                   {"notif": self.notification.id_hash})
        self.assertEqual(request.status_code, 200)

    def test_no_user_delete_view(self):
        request = self.client.post('/delete/',
                                   {"id": self.notification.id_hash})
        self.assertNotEqual(request.status_code, 200)

    def test_other_user_delete_view(self):
        self.client.login(username='testuser2', password='test')
        request = self.client.post('/delete/',
                                   {"id": self.notification.id_hash})
        self.assertEqual(request.status_code, 403)

    def test_valid_user_delete_view(self):
        self.client.login(username='testuser', password='test')
        un_id = self.notification.id_hash
        self.client.post('/delete/', {"id": self.notification.id_hash})
        self.assertFalse(Notification.objects.filter(id_hash=un_id).count())
