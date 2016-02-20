"""mjworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.index', name='core_index'),
    url(r'^verify/', 'core.views.verify', name='core_verify'),
    url(r'^home/', 'core.views.home', name='core_home'),
    url(r'^userprofile/', include('userdetails.urls',
                                  namespace='userprofile')),
    url(r'^customer/', include('customer.urls', namespace='customer')),
    url(r'^part/', include('parts.urls', namespace='part')),
    url(r'^vehical/', include('vehical.urls', namespace='vehical')),
    url(r'^service/', include('service.urls', namespace='service')),
    url(r'^mechanic/', include('mechanic.urls', namespace='mechanic')),
    url(r'^login/$', 'userdetails.views.login',
        name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout'),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
