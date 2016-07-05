from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from .models import Category
from .views import category


class CategoriesViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester",
                                             email="smt@smt.com",
                                             password="top_secret")
        self.category = Category.objects.create(name="TestCategory",
                                                path_bg="test",
                                                path_banner="test",
                                                path_icon="tes",
                                                path_mini="test")
        self.category.save()

    def test_valid_view(self):
        request = self.factory.get('/category')
        request.user = self.user
        status = category(request, "TestCategory")
        self.assertEqual(status, 200)

    def test_invalid_view(self):
        request = self.factory.get('/category')
        request.user = self.user
        status = category(request, "Blablabla")
        self.assertEqual(status, 404)
