import os
from forms import UserForm
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.test import TestCase
from django.test.client import Client
from models import URL

class SimpleTest(TestCase):
    def test_details(self):
        client = Client()
        response = client.get('')
        self.failUnlessEqual(response.status_code, 200)
        self.failIfEqual(response.context['form'], None, "No customer in context")
    
    def test_middleware(self):
        count = URL.objects.count()
        client = Client()
        client.get('')
        count = URL.objects.count() - count
        self.failIfEqual(count, 0, "Middleware don't work")
        url=URL.objects.latest('pk')
        self.failUnlessEqual(url.url, 'testserver/', "Middleware don't work")
        
    def test_context_processor(self):
        client = Client()
        response = client.get('')
        self.failIfEqual(response.context['django.settings'], None, "Context processor don't work")
        
    def test_form_valid(self):
        client = Client()
        form = UserForm()
        post_data = {
            'form': form
        }
        response = client.post('', post_data)
        self.failUnlessEqual(response.status_code, 200)