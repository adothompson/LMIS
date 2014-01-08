#import external modules
from rest_framework import serializers

#import project modules
from core.models import (Product, ProductCategory, UnitOfMeasurement, UOMCategory, CompanyCategory, Company,
                         Currency)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API Serializer for Product models
    """
    class Meta:
        model = Product


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API Serializer for ProductCategory model
    """
    class Meta:
        model = ProductCategory


class UnitOfMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API Serializer for UnitOfMeasurement model
    """
    class Meta:
        model = UnitOfMeasurement


class UOMCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API Serializer for UOMCategory model
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
        REST API serializer for Company model
    """
    class Meta:
        model = Company


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API serializer for Currency model
    """
    class Meta:
        model = Currency