#import external modules
from rest_framework import serializers

#import project modules
from .models import Product, ProductCategory, UnitOfMeasurement, UOMCategory


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
        Serializer for product models
    """
    class Meta:
        model = Product


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
        Serializer for Product Category
    """
    class Meta:
        model = ProductCategory


class  UnitOfMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    """
        Serializer for UnitOfMeasurement
    """
    class Meta:
        model = UnitOfMeasurement


class UOMCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
        Serializer for UnitOfMeasurement
    """
    class Meta:
        model = UOMCategory