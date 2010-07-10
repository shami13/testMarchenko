from django.contrib import admin
from django.conf.urls.defaults import include, patterns

import views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.main_page),
    (r'^/main/$', views.main_page),
    (r'^main/$', views.main_page),
    (r'^main$', views.main_page),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
)
