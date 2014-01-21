#import core Django modules
from django.conf.urls import patterns, url, include

#import external modules
from rest_framework import routers

#import LMIS modules
from . import views

router = routers.DefaultRouter()
router.register(r'facility-supported-program-product', views.FacilitySupportedProgramProductViewSet)
router.register(r'supervisory-node', views.SupervisoryNodeViewSet)
router.register(r'order-group', views.OrderGroupViewSet)
router.register(r'facility-supported-program', views.FacilitySupportedProgramViewSet)
router.register(r'facility-type', views.FacilityTypeViewSet)
router.register(r'facility', views.FacilityViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    )