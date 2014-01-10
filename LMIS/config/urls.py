#import core django modules
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from core.views import DashboardIndex


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', DashboardIndex.as_view(), name='index_dashboard'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'api/v1/core/', include('core.urls')),
                       url(r'api/v1/cce/', include('cce.urls')))
