from django.conf.urls import patterns, include, url

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'^program', views.ProgramViewSet)
router.register(r'^programproduct', views.ProgramProductAllocationInfoViewSet)
router.register(r'programproductallocationinfo', views.ProgramProductAllocationInfoViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)