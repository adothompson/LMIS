"""
    Serializer for Inventory App related API end-points
"""

#import LMIS project modules
from core.api.serializers import BaseModelSerializer
from inventory.models import Inventory, InventoryLine


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