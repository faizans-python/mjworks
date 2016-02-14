from django.conf.urls import patterns, url

from mechanic.views import *


urlpatterns = patterns(
    '',
    url(r'^add/$', 'mechanic.views.add_mechanic',
        name='add_mechanic'),
)
