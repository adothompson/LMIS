"""
    This module defines URL routing for Inventory REST API
"""

#import core Django modules
from django.conf.urls import patterns, url, include

#import external modules
from rest_framework import routers

#create core REST API routers
from . import views

router = routers.DefaultRouter()
router.register(r'^inventory', views.InventoryViewSet)
router.register(r'^inventory-lines', views.InventoryLineViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)