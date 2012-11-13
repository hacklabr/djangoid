from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('server.views',
    url(r'^', 'endpoint'),
    url(r'^yadis/$', 'serveryadis'),
)
