"""
    core/api/serializers.py is the module for core model api data serializers
"""

#import core django module
from django.contrib.auth.models import User, Permission

#import external modules
from rest_framework import serializers

#import project modules
from core.models import (Product, ProductCategory, UnitOfMeasurement, UOMCategory, CompanyCategory, Company,
                         Currency, Rate, Contact, Address, EmployeeCategory, Employee, ProductPresentation,
                         ModeOfAdministration, ProductItem, ProductFormulation)


class UserSerializer(serializers.ModelSerializer):
    """
        REST API serializer for User model
    """
    class Meta:
        model = User


class BaseModelSerializer(serializers.ModelSerializer):
    """
        Base Model Serializer for models
    """
    created_by = UserSerializer(required=False, read_only=True)
    modified_by = UserSerializer(required=False, read_only=True)


class ProductCategorySerializer(BaseModelSerializer):
    """
        REST API Serializer for ProductCategory model
    """
    class Meta:
        model = ProductCategory


class ProductSerializer(BaseModelSerializer):
    """
        REST API Serializer for Product models
    """
    class Meta:
        model = Product


class UOMCategorySerializer(BaseModelSerializer):
    """
        REST API Serializer for UOMCategory model
    """
    class Meta:
        model = UOMCategory


class UnitOfMeasurementSerializer(BaseModelSerializer):
    """
        REST API Serializer for UnitOfMeasurement model
    """
    class Meta:
        model = UnitOfMeasurement


class CompanyCategorySerializer(BaseModelSerializer):
    """
        REST API serializer for CompanyCategory model
    """
    class Meta:
        model = CompanyCategory


class CompanySerializer(BaseModelSerializer):
    """
        REST API serializer for Company model
    """
    class Meta:
        model = Company


class CurrencySerializer(BaseModelSerializer):
    """
        REST API serializer for Currency model
    """
    class Meta:
        model = Currency
        fields = ('code', 'name', 'symbol', 'symbol_position', 'rates',)


class RateSerializer(BaseModelSerializer):
    """
        REST API serializer for Rate model
    """
    class Meta:
        model = Rate


class ContactSerializer(BaseModelSerializer):
    """
        REST API serializer for Contact model
    """
    class Meta:
        model = Contact


class AddressSerializer(BaseModelSerializer):
    """
        REST  API serializer for Address model
    """
    class Meta:
        model = Address


class EmployeeCategorySerializer(BaseModelSerializer):
    """
        REST API serializer for EmployeeCategory
    """
    class Meta:
        model = EmployeeCategory


class EmployeeSerializer(BaseModelSerializer):
    """
        REST API serializer for Employee
    """
    class Meta:
        model = Employee


class PermissionSerializer(BaseModelSerializer):
    """
        REST API serializer for Permission model
    """
    class Meta:
        model = Permission


class ProductPresentationSerializer(BaseModelSerializer):
    """
        REST API serializer for ProductPresentation model
    """
    class Meta:
        model = ProductPresentation


class ModeOfAdministrationSerializer(BaseModelSerializer):
    """
        REST API serializer for ModeOfAdministration model
    """
    class Meta:
        model = ModeOfAdministration


class ProductItemSerializer(BaseModelSerializer):
    """
        REST API serializer for ProductItem model
    """
    class Meta:
        model = ProductItem


class ProductFormulationSerializer(BaseModelSerializer):
    """
        REST API serializer for ProductFormulation model, it can be Lyophilized, Liquid or Not Applicable
    """
    class Meta:
        model = ProductFormulation

