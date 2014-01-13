#import core django modules
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'api/v1/core/', include('core.api.urls')),
                       url(r'api/v1/cce/', include('cce.api.urls')),
                       url(r'api/v1/facilities/', include('facilities.api.urls')),
<<<<<<< HEAD

                       # DRF browsable API urls
                       url(r'^api-web/', include('rest_framework.urls', namespace='rest_framework'))
)
=======
                       url(r'api/v1/inventory/', include('inventory.api.urls')),)
>>>>>>> 6c3dbb4ce21b85ebf68be28887a4cf697b0e6c6f
