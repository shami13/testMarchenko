from django.contrib import admin
from django.conf.urls.defaults import include, patterns, url

import views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.main_page),         
    url(r'^urllist', 'testMarchenko.views.url_list'),          
    url(r'^main', 'testMarchenko.views.main_page'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/', include('accounts.urls')),
)
