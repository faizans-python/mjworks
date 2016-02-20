from django.conf.urls import patterns, url

from service.views import *


urlpatterns = patterns(
    '',
    url(r'^add/$', 'service.views.service_add',
        name='service_add'),
    url(r'^create/$', 'service.views.service_create',
        name='service_create'),
)
