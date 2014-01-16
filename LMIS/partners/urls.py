from django.conf.urls import patterns, include, url

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'^program', views.ProgramViewSet)
router.register(r'^program-product', views.ProgramProductAllocationInfoViewSet)
router.register(r'program-product-allocation-info', views.ProgramProductAllocationInfoViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)