#import external modules
from rest_framework import serializers

#import project modules
from core.models import Product, ProductCategory, UnitOfMeasurement, UOMCategory, CompanyCategory, Company


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API Serializer for product models
    """
    class Meta:
        model = Product


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API Serializer for Product Category
    """
    class Meta:
        model = ProductCategory


class UnitOfMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API Serializer for UnitOfMeasurement
    """
    class Meta:
        model = UnitOfMeasurement


class UOMCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API Serializer for UOMCategory
    """
    class Meta:
        model = UOMCategory


class CompanyCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API serializer for CompanyCategory model
    """
    class Meta:
        model = CompanyCategory


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API serializer for CompanySerializer
    """
    class Meta:
        model = Company