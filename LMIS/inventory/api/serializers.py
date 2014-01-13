"""
    Serializer for Inventory App related API end-points
"""

#import LMIS project modules
from core.api.serializers import BaseModelSerializer
from inventory.models import Inventory, InventoryLine, ConsumptionRecord, ConsumptionRecordLine


class InventorySerializer(BaseModelSerializer):
    """
        Inventory Model serializer
    """
    class Meta:
        model = Inventory


class InventoryLineSerializer(BaseModelSerializer):
    """
        Inventory Line serializer for Inventory model
    """
    class Meta:
        model = InventoryLine


class ConsumptionRecordSerializer(BaseModelSerializer):
    """
        Consumption Record Serializer used by the API endpoint to serialize Consumption record
    """
    class Meta:
        model = ConsumptionRecord


class ConsumptionRecordLineSerializer(BaseModelSerializer):
    """
        ConsumptionRecordLine Serializer used by the API end-point to serialize ConsumptionRecordLine record
    """
    class Meta:
        model = ConsumptionRecordLine