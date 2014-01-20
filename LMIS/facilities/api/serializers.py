"""
    core/api/serializers.py is the module for core model api data serializers
"""

#import LMIS project module
from core.api.serializers import BaseModelSerializer, ProductSerializer
from facilities.models import (FacilityType, Facility, FacilitySupportedProgram, FacilitySupportedProgramProduct,
                                SupervisoryNode, OrderGroup, WarehouseType, Warehouse,
                                 FacilityProgramProductParameter)


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
    products = ProductSerializer(read_only=True)

    class Meta:
        model = Facility



class FacilitySupportedProgramSerializer(BaseModelSerializer):
    """
        REST API serializer for FacilitySupportedProgram model
    """
    class Meta:
        model = FacilitySupportedProgram


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


class  FacilityProgramProductParameterSerializer(BaseModelSerializer):
    class Meta:
        model =  FacilityProgramProductParameter