from django.contrib import admin
from django.conf.urls.defaults import include, patterns, url

import views
import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.main_page),         
    url(r'^urllist', 'testMarchenko.views.url_list'),          
    (r'^main/$', views.main_page),
    url(r'^main', 'testMarchenko.views.main_page'),
    url(r'^ajax_request', 'testMarchenko.views.ajax_request'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/', include('accounts.urls')),
    (r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    )