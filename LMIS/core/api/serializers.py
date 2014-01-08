#import core django module
from django.contrib.auth.models import User

#import external modules
from rest_framework import serializers

#import project modules
from core.models import (Product, ProductCategory, UnitOfMeasurement, UOMCategory, CompanyCategory, Company,
                         Currency, Rate, Contact, Address, EmployeeCategory, Employee)


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


class RateSerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API serializer for Rate model
    """
    class Meta:
        model = Rate


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API serializer for Contact model
    """
    class Meta:
        model = Contact


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    """
        REST  API serializer for Address model
    """
    class Meta:
        model = Address


class EmployeeCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API serializer for EmployeeCategory
    """
    class Meta:
        model = EmployeeCategory


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API serializer for Employee
    """
    class Meta:
        model = Employee


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
        REST API serializer for User model
    """
    class Meta:
        model = User