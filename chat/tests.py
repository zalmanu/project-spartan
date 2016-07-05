from django.test import TestCase


class ChatTestCase(TestCase):
    def test_calls_views_denies_anonymous(self):
        response = self.client.get('/mail/', follow=True)
        self.assertRedirects(response, '/login/?next=/mail/')
