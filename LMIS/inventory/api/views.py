"""
    This module hold Inventory App API view end-point and the view set
"""

#import LMIS project modules
from core.api.views import BaseModelViewSet
from inventory.models import Inventory, InventoryLine
from .serializers import InventorySerializer, InventoryLineSerializer


class InventoryViewSet(BaseModelViewSet):
    """
        API end-point that CRUD and ad-hoc functions to be performed on the Inventory objects via API
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryLineViewSet(BaseModelViewSet):
    """
        API end point for Inventory Lines
    """
    queryset = InventoryLine.objects.all()
    serializer_class = InventoryLineSerializer