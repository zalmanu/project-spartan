from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from authentication.models import Account
from .models import Announcement
from .views import post, edit_post


class PostsViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester",
                                             email="smt@smt.com",
                                             password="top_secret")
        self.user.save()
        self.user2 = User.objects.create_user(username="testerspartan",
                                              email="smt@gmail.com",
                                              password="top_secret2")
        self.user2.save()
        account = Account.objects.create(city="Timisoara", country="Romania",
                                         user=self.user)
        account.save()
        account2 = Account.objects.create(city="Timisoara",
                                          country="Romania",
                                          user=self.user2)
        account2.save()
        self.post = Announcement.objects.create(title="Zugrav",
                                                text="Asa de un zugrav",
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
