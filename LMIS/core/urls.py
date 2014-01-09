from django.conf.urls import patterns, url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'^product', views.ProductViewSet)
router.register(r'^product-category', views.ProductCategoryViewSet)
router.register(r'uom', views.UnitOfMeasurementViewSet)
router.register(r'uom-category', views.UOMCategoryViewSet)
router.register(r'company-category', views.CompanyCategoryViewSet)
router.register(r'company', views.CompanyViewSet)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'rate', views.RateViewSet)
router.register(r'contact', views.ContactViewSet)
router.register(r'address', views.AddressViewSet)
router.register(r'employee-category', views.EmployeeCategoryViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'permission', views.PermissionViewSet)
router.register(r'facility-type', views.FacilityTypeViewSet)
router.register(r'facility', views.FacilityViewSet)
router.register(r'program', views.ProgramViewSet)
router.register(r'program-products', views.ProgramProductViewSet)
router.register(r'facility-supported-program', views.FacilitySupportedProgramViewSet)
router.register(r'program-product-allocation-info', views.ProgramProductAllocationInfoViewSet)
router.register(r'facility-supported-program-product', views.FacilitySupportedProgramProductViewSet)
router.register(r'supervisory-node', views.SupervisoryNodeViewSet)
router.register(r'order-group', views.OrderGroupViewSet)
router.register(r'product-presentation', views.ProductPresentationViewSet)
router.register(r'mode-of-administration', views.ModeOfAdministrationViewSet)
router.register(r'warehouse-type', views.WarehouseTypeViewSet)
router.register(r'warehouse', views.WarehouseViewSet)
router.register(r'product-item', views.ProductItemViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    # Additionally, we include login URLs for the browse-able API.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)