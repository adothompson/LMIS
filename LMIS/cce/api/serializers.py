"""
    This module holds CCE app Model Serializers
"""

#import external modules
from rest_framework import serializers

#import project modules
from core.api.serializers import BaseModelSerializer
from cce.models import ColdChainEquipment, ColdChainEquipmentType


class CCESerializer(BaseModelSerializer):
    """
        This is serializer for ColdChainEquipment model
    """
    class Meta:
        model = ColdChainEquipment


class CCETypeSerializer(BaseModelSerializer):
    """
        This is serializer for ColdChainEquipmentType model
    """
    class Meta:
        model = ColdChainEquipmentType
