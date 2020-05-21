from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class DefaultTest(TestCase):

    def test_default(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 404)
