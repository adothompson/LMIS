"""
    core/api/serializers.py is the module for core model api data serializers
"""

#import core django module
from django.contrib.auth.models import User, Permission

#import external modules
from rest_framework import serializers

#import project modules
from core.models import (Product, ProductCategory, UnitOfMeasurement, UOMCategory, CompanyCategory, Company,
                         Currency, Rate, Contact, Address, EmployeeCategory, Employee, FacilityType, Facility, Program,
                         ProgramProduct, FacilitySupportedProgram, ProgramProductAllocationInfo,
                         FacilitySupportedProgramProduct, SupervisoryNode, OrderGroup, ProductPresentation,
                         ModeOfAdministration, WarehouseType, Warehouse, ProductItem
                         )


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


class ProductCategorySerializer(serializers.ModelSerializer):
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


class FacilityTypeSerializer(BaseModelSerializer):
    """
        REST API serializer for FacilityType model
    """
    class Meta:
        model = FacilityType


class FacilitySerializer(BaseModelSerializer):
    """
        REST API serializer for Facility model
    """
    class Meta:
        model = Facility


class ProgramSerializer(BaseModelSerializer):
    """
        REST API serializer for Program model
    """
    class Meta:
        model = Program


class ProgramProductSerializer(BaseModelSerializer):
    """
        REST API serializer for ProgramProduct model
    """
    class Meta:
        model = ProgramProduct


class FacilitySupportedProgramSerializer(BaseModelSerializer):
    """
        REST API serializer for FacilitySupportedProgram model
    """
    class Meta:
        model = FacilitySupportedProgram


class ProgramProductAllocationInfoSerializer(BaseModelSerializer):
    """
        REST API  serializer for ProgramProductAllocationInfo model
    """
    class Meta:
        model = ProgramProductAllocationInfo


class FacilitySupportedProgramProductSerializer(BaseModelSerializer):
    """
        REST API serializer for FacilitySupportedProgramProduct model
    """
    class Meta:
        model = FacilitySupportedProgramProduct


class SupervisoryNodeSerializer(BaseModelSerializer):
    """
       REST API serializer for SupervisoryNode model
    """
    class Meta:
        model = SupervisoryNode


class OrderGroupSerializer(BaseModelSerializer):
    """
        REST API serializer for OrderGroup model
    """
    class Meta:
        model = OrderGroup


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


class WarehouseTypeSerializer(BaseModelSerializer):
    """
        REST API serializer for WarehouseType model
    """
    class Meta:
        model = WarehouseType


class WarehouseSerializer(BaseModelSerializer):
    """
        REST API serializer for Warehouse model
    """
    class Meta:
        model = Warehouse


class ProductItemSerializer(BaseModelSerializer):
    """
        REST API serializer for ProductItem model
    """
    class Meta:
        model = ProductItem

