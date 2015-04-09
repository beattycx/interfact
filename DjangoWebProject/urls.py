"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from app.forms import BootstrapAuthenticationForm
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import HomeRegistrationView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^interfact/$', 'app.views.base', name='base'),
    url(r'^accounts/register/$', HomeRegistrationView.as_view(), name='labmgmt'),
    url(r'^interfact/labmgmt/$', 'app.views.labmgmt', name='registration_register'),
    url(r'^interfact/labmgmt/order/$', 'app.views.order', name='order'),
    url(r'^interfact/labmgmt/order/sample_details/$', 'app.views.sample_details', name='sample_details'),
    (r'^accounts/', include('registration.backends.simple.urls')), #TODO email auth

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
