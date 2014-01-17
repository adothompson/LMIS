from django.conf.urls import patterns, include, url

from rest_framework import routers

from LMIS.partners.api import views


router = routers.DefaultRouter()
router.register(r'^program', views.ProgramViewSet)
router.register(r'^program-product', views.ProgramProductViewSet)
router.register(r'program-product-allocation-info', views.ProgramProductAllocationInfoViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)