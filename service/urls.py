from django.conf.urls import patterns, url

from service.views import *


urlpatterns = patterns(
    '',
    url(r'^add/$', 'service.views.service_add',
        name='service_add'),
    url(r'^create/$', 'service.views.service_create',
        name='service_create'),
    url(r'^search/$', 'service.views.service_search',
        name='service_search'),
    url(r'^view/(?P<id>[0-9]+)/$', 'service.views.service_view',
        name='service_view'),
    url(r'^pending/$', 'service.views.service_pending',
        name='service_pending'),
)
