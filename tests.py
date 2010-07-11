import os
from django.contrib.auth.models import User
from templatetags.edit_list import edit_list
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
    
    def test_field_sort(self):
        client = Client()
        client.post('/accounts/login/', {'username' : 'admin', 'password':'password'})
        response = client.get('')
        self.failUnlessEqual(response.context['form'].fields.keyOrder[0], 'birthDate')
        
    def test_edit_list_tag(self):
        user = User.objects.latest('pk')
        self.failUnlessEqual(edit_list(user), '<a href="/admin/auth/User/2"> edit User</a>', 'edit_list fail')