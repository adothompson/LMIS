"""
    This module holds CCE app Model Serializers
"""

#import external modules
from rest_framework import serializers

#import project modules
from core.api.serializers import BaseModelSerializer
from cce.models import ColdChainEquipment


class CCESerializer(BaseModelSerializer):
    """
        This is serializer for CCE model
    """
    class Meta:
        model = ColdChainEquipment