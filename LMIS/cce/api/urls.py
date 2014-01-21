"""
    This modules defines CCE app API urls
"""
from django.conf.urls import patterns, url, include
from rest_framework import routers


#create cce app REST API routers and urls
from . import views

router = routers.DefaultRouter()
router.register(r'storage-location', views.StorageLocationViewSet)
router.register(r'storage-location-type', views.StorageLocationTypeViewSet)
router.register(r'storage-location-temp-log', views.StorageLocationTempLogViewSet)
router.register(r'storage-location-problem-log', views.StorageLocationProblemLogViewSet)


# Wire up our API using automatic URL routing.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)