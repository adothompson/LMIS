"""
    This modules defines CCE app API urls
"""
from django.conf.urls import patterns, url, include
from rest_framework import routers


#create cce app REST API routers and urls
from . import views

router = routers.DefaultRouter()
router.register(r'cce', views.CCEViewSet)
router.register(r'cce-type', views.CCETypeViewSet)
router.register(r'cce-temp-log', views.CCETemperatureLogViewSet)
router.register(r'cce-problem-log', views.CCEProblemLogViewSet)


# Wire up our API using automatic URL routing.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)