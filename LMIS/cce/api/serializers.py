"""
    This module holds CCE app Model Serializers
"""

#import external modules
from rest_framework import serializers

#import project modules
from core.api.serializers import BaseModelSerializer
from cce.models import StorageLocation, StorageLocationType, StorageLocationTempLog, StorageLocationProblemLog


class StorageLocationSerializer(BaseModelSerializer):
    """
        This is serializer for StorageLocation model
    """
    class Meta:
        model = StorageLocation


class StorageLocationTypeSerializer(BaseModelSerializer):
    """
        This is serializer for StorageLocationType model
    """
    class Meta:
        model = StorageLocationType


class StorageLocationTempLogSerializer(BaseModelSerializer):
    """
        This is serializer for StorageLocationTempLog model
    """
    class Meta:
        model = StorageLocationTempLog


class StorageLocationProblemLogSerializer(BaseModelSerializer):
    """
        This is serializer for StorageLocationProblemLog model
    """
    class Meta:
        model = StorageLocationProblemLog
