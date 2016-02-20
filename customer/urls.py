from django.conf.urls import patterns, url

from customer.views import *


urlpatterns = patterns(
    '',
    url(r'^add/$', 'customer.views.add_customer',
        name='add_customer'),
    url(r'^create/$', 'customer.views.customer_create',
        name='customer_create'),
    url(r'^view/$', 'customer.views.customer_view',
        name='customer_view'),
)
