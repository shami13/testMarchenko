import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.test import TestCase
from django.test.client import Client

class SimpleTest(TestCase):
    def test_details(self):
        client = Client()
        response = client.get('')
        self.failUnlessEqual(response.status_code, 200)
        self.failIfEqual(response.context['customer'], None, "No customer in context")