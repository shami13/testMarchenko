import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.test import TestCase
from django.test.client import Client
from models import URL

class SimpleTest(TestCase):
    def test_details(self):
        client = Client()
        client.post('/accounts/login/', {'username' : 'admin', 'password':'password'})
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
        client.post('/accounts/login/', {'username' : 'admin', 'password':'password'})
        response = client.get('')
        self.failIfEqual(response.context['django.settings'], None, "Context processor don't work")
        
    def test_auth(self):
        client = Client()
        response = client.get('')
        self.failUnlessEqual(response.status_code, 302)
        
    def test_calendar_widget(self):
        client = Client()
        client.post('/accounts/login/', {'username' : 'admin', 'password':'password'})
        response = client.get('')
        self.failUnless('type="text/javascript" src="/media/jquery-1.4.2.min.js"' in response.content, 'no library jquery')
        self.failUnless('type="text/javascript" src="/media/jquery.ui.core.js"' in response.content, 'no library jquery.ui.core')
        self.failUnless('type="text/javascript" src="/media/jquery.ui.datepicker.js' in response.content, 'no library jquery.ui.datepicker.js')
        self.failUnless('.datepicker(' in response.content, "don't used jquery datepicker")
        