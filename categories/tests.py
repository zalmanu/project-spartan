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
