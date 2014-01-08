from django.conf.urls import patterns, url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'productcategory', views.ProductCategoryViewSet)
router.register(r'uom', views.UnitOfMeasurementViewSet)
router.register(r'uomcategory', views.UOMCategoryViewSet)
router.register(r'companycategory', views.CompanyCategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)