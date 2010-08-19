import os
from management.commands.printmodels import print_modles
from django.db import models
import string
from django.contrib.auth.models import User
from templatetags.edit_list import edit_list
from forms import UserForm
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
        self.failUnless('.datepicker();' in response.content, 'no library jquery')
        
    
    def test_field_sort(self):
        client = Client()
        client.post('/accounts/login/', {'username' : 'admin', 'password':'password'})
        response = client.get('')
        self.failUnlessEqual(response.context['form'].fields.keyOrder[0], 'birthDate')
        
    def test_command(self):
        result = print_modles(models.get_app('testMarchenko'))
        self.failUnlessEqual(string.find(result, "User 1"), 0, "Change db or fail script")
    def test_edit_list_tag(self):
        user = User.objects.latest('pk')
        self.failUnlessEqual(edit_list(user), '<a href="/admin/auth/User/2"> edit User</a>', 'edit_list fail')
