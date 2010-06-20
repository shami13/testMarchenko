import views
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    ('', views.main_page),
    (r'^main/$', views.main_page),
)
