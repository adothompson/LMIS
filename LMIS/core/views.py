#import external modules
from rest_framework import viewsets

#import project modules
from .models import (Product, ProductCategory, UnitOfMeasurement, UOMCategory, CompanyCategory, Company)
from .api.serializers import (ProductSerializer, ProductCategorySerializer, UnitOfMeasurementSerializer,
                              UOMCategorySerializer, CompanyCategorySerializer, CompanySerializer)


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