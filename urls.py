from django.contrib import admin
from django.conf.urls.defaults import include, patterns

import views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^main/$', views.main_page),
    (r'^main$', views.main_page),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin', include(admin.site.urls)),
)
