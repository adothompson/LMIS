"""
    Serializer for Inventory App related API end-points
"""

#import LMIS project modules
from core.api.serializers import BaseModelSerializer
from inventory.models import (Inventory, InventoryLine, ConsumptionRecord, ConsumptionRecordLine, IncomingShipment,
                              IncomingShipmentLine, OutgoingShipment, OutgoingShipmentLine)


class InventoryLineSerializer(BaseModelSerializer):
    """
        Inventory Line serializer for Inventory records
    """

    class Meta:
        model = InventoryLine


class InventorySerializer(BaseModelSerializer):
    """
        Inventory Model serializer
    """
    class Meta:
        model = Inventory
        fields = ('warehouse', 'cce', 'inventory_lines', 'is_deleted',)


class ConsumptionRecordSerializer(BaseModelSerializer):
    """
        Consumption Record Serializer used by the API endpoint to serialize Consumption records
    """
    class Meta:
        model = ConsumptionRecord


class ConsumptionRecordLineSerializer(BaseModelSerializer):
    """
        ConsumptionRecordLine Serializer used by the API end-point to serialize ConsumptionRecordLine records
    """
    class Meta:
        model = ConsumptionRecordLine


class IncomingShipmentSerializer(BaseModelSerializer):
    """
        IncomingShipmentSerializer used by the API end-point
    """
    class Meta:
        model = IncomingShipment


class IncomingShipmentLineSerializer(BaseModelSerializer):
    """
        IncomingShipmentSerializer used by the API end-point
    """
    class Meta:
        model = IncomingShipmentLine


class OutgoingShipmentSerializer(BaseModelSerializer):
    """
        OutgoingShipmentSerializer is used by the API end-point to serialize OutgoingShipment records
    """
    class Meta:
        model = OutgoingShipment


class OutgoingShipmentLineSerializer(BaseModelSerializer):
    """
        OutgoingShipmentLineSerializer is used by the API end-points to serialize OutgoingShipmentLine records
    """
    class Meta:
        model = OutgoingShipmentLine
