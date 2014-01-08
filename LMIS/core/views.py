#import from django core modules
from django.contrib.auth.models import User, Permission

#import external modules
from rest_framework import viewsets

#import project modules
from .models import (Product, ProductCategory, UnitOfMeasurement, UOMCategory, CompanyCategory, Company, Rate, Contact,
                     Address, EmployeeCategory, Employee, FacilityType)

from .api.serializers import (ProductSerializer, ProductCategorySerializer, UnitOfMeasurementSerializer,
                              UOMCategorySerializer, CompanyCategorySerializer, CompanySerializer, CurrencySerializer,
                              RateSerializer, ContactSerializer, AddressSerializer, EmployeeCategorySerializer,
                              EmployeeSerializer, UserSerializer, PermissionSerializer, FacilityTypeSerializer)


#TODO: add view function that returns only deleted models and make normal query set to return only models not yet
#TODO: deleted
#TODO: over-ride ModelViewSet.destroy() to return just turn on model is_deleted flag on(soft delete)

class ProductViewSet(viewsets.ModelViewSet):
    """
        API end-point that allows list of all products to be view
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
        API end point for product category
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class UnitOfMeasurementViewSet(viewsets.ModelViewSet):
    """
       API end point for Unit of Measurement
    """
    queryset = UnitOfMeasurement.objects.all()
    serializer_class = UnitOfMeasurementSerializer


class UOMCategoryViewSet(viewsets.ModelViewSet):
    """
        API end point for unit of measurement category
    """
    queryset = UOMCategory.objects.all()
    serializer_class = UOMCategorySerializer


class CompanyCategoryViewSet(viewsets.ModelViewSet):
    """
        API end point for Company Category
    """
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
        API end point for Company
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    """
        API end point for Currency model
    """
    queryset = Company.objects.all()
    serializer_class = CurrencySerializer


class RateViewSet(viewsets.ModelViewSet):
    """
        API end-point for Rate model
    """
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
        API end-point for Contact model
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
        API end point for Address Model
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class EmployeeCategoryViewSet(viewsets.ModelViewSet):
    """
        API end point for EmployeeCategory model
    """
    queryset = EmployeeCategory.objects.all()
    serializer_class = EmployeeCategorySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
        API end point for Employee model
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        API end point User model, required by EmployeeViewSet
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """
        API end-point for Permission model required by UserViewSet since User model references Permission
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class FacilityTypeViewSet(viewsets.ModelViewSet):
    """
        API end-point for FacilityType model.
    """
    queryset = FacilityType.objects.all()
    serializer_class = FacilityTypeSerializer