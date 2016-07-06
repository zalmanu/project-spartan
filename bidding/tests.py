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
                                         cui="dwda",
                                         bank="1234123412341234",
                                         user=self.spartan,
                                         spartanStatus=True)
        spartan.save()
        self.post = Announcement.objects.create(title="Zugrav",
                                                text="Asa de un zugrav",
                                                author=self.user,
                                                price=200)
        self.post.save()
        self.offer = Offer.objects.create(price=20,
                                          spartan=self.spartan.spartan,
                                          post=self.post, kind="/job")
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
