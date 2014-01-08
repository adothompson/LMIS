#import core django module
from django.contrib.auth.models import User, Permission

#import external modules
from rest_framework import serializers

#import project modules
from core.models import (Product, ProductCategory, UnitOfMeasurement, UOMCategory, CompanyCategory, Company,
                         Currency, Rate, Contact, Address, EmployeeCategory, Employee, FacilityType, Facility)


class ProductCategorySerializer(serializers.ModelSerializer):
    """
        REST API Serializer for ProductCategory model
    """
    class Meta:
        model = ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    """
        REST API Serializer for Product models
    """
    class Meta:
        model = Product


class UOMCategorySerializer(serializers.ModelSerializer):
    """
        REST API Serializer for UOMCategory model
    """
    class Meta:
        model = UOMCategory


class UnitOfMeasurementSerializer(serializers.ModelSerializer):
    """
        REST API Serializer for UnitOfMeasurement model
    """
    class Meta:
        model = UnitOfMeasurement


class CompanyCategorySerializer(serializers.ModelSerializer):
    """
        REST API serializer for CompanyCategory model
    """
    class Meta:
        model = CompanyCategory


class CompanySerializer(serializers.ModelSerializer):
    """
        REST API serializer for Company model
    """
    class Meta:
        model = Company


class CurrencySerializer(serializers.ModelSerializer):
    """
        REST API serializer for Currency model
    """
    class Meta:
        model = Currency


class RateSerializer(serializers.ModelSerializer):
    """
        REST API serializer for Rate model
    """
    class Meta:
        model = Rate


class ContactSerializer(serializers.ModelSerializer):
    """
        REST API serializer for Contact model
    """
    class Meta:
        model = Contact


class AddressSerializer(serializers.ModelSerializer):
    """
        REST  API serializer for Address model
    """
    class Meta:
        model = Address


class EmployeeCategorySerializer(serializers.ModelSerializer):
    """
        REST API serializer for EmployeeCategory
    """
    class Meta:
        model = EmployeeCategory


class EmployeeSerializer(serializers.ModelSerializer):
    """
        REST API serializer for Employee
    """
    class Meta:
        model = Employee


class UserSerializer(serializers.ModelSerializer):
    """
        REST API serializer for User model
    """
    class Meta:
        model = User


class PermissionSerializer(serializers.ModelSerializer):
    """
        REST API serializer for Permission model
    """
    class Meta:
        model = Permission


class FacilityTypeSerializer(serializers.ModelSerializer):
    """
        REST API serializer for FacilityType model
    """
    class Meta:
        model = FacilityType


class FacilitySerializer(serializers.ModelSerializer):
    """
        REST API serializer for Facility model
    """
    class Meta:
        model = Facility
