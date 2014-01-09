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
                         ModeOfAdministration, WarehouseType, Warehouse
                         )


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


class ProgramSerializer(serializers.ModelSerializer):
    """
        REST API serializer for Program model
    """
    class Meta:
        model = Program


class ProgramProductSerializer(serializers.ModelSerializer):
    """
        REST API serializer for ProgramProduct model
    """
    class Meta:
        model = ProgramProduct


class FacilitySupportedProgramSerializer(serializers.ModelSerializer):
    """
        REST API serializer for FacilitySupportedProgram model
    """
    class Meta:
        model = FacilitySupportedProgram


class ProgramProductAllocationInfoSerializer(serializers.ModelSerializer):
    """
        REST API  serializer for ProgramProductAllocationInfo model
    """
    class Meta:
        model = ProgramProductAllocationInfo


class FacilitySupportedProgramProductSerializer(serializers.ModelSerializer):
    """
        REST API serializer for FacilitySupportedProgramProduct model
    """
    class Meta:
        model = FacilitySupportedProgramProduct


class SupervisoryNodeSerializer(serializers.ModelSerializer):
    """
       REST API serializer for SupervisoryNode model
    """
    class Meta:
        model = SupervisoryNode


class OrderGroupSerializer(serializers.ModelSerializer):
    """
        REST API serializer for OrderGroup model
    """
    class Meta:
        model = OrderGroup


class ProductPresentationSerializer(serializers.ModelSerializer):
    """
        REST API serializer for ProductPresentation model
    """
    class Meta:
        model = ProductPresentation


class ModeOfAdministrationSerializer(serializers.ModelSerializer):
    """
        REST API serializer for ModeOfAdministration model
    """
    class Meta:
        model = ModeOfAdministration


class WarehouseTypeSerializer(serializers.ModelSerializer):
    """
        REST API serializer for WarehouseType model
    """
    class Meta:
        model = WarehouseType


class WarehouseSerializer(serializers.ModelSerializer):
    """
        REST API serializer for Warehouse model
    """
    class Meta:
        model = Warehouse