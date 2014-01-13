"""
    This module hold Inventory App API view end-point and the view set
"""

#import LMIS project modules
from core.api.views import BaseModelViewSet
from inventory.models import (Inventory, InventoryLine, ConsumptionRecord, ConsumptionRecordLine, IncomingShipment,
                              IncomingShipmentLine, OutgoingShipment)
from .serializers import (InventorySerializer, InventoryLineSerializer, ConsumptionRecordSerializer,
                          ConsumptionRecordLineSerializer, IncomingShipmentSerializer, IncomingShipmentLineSerializer,
                          OutgoingShipmentSerializer)


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


class ConsumptionRecordViewSet(BaseModelViewSet):
    """
        API end-point for Consumption API
    """
    queryset = ConsumptionRecord.objects.all()
    serializer_class = ConsumptionRecordSerializer


class ConsumptionRecordLineViewSet(BaseModelViewSet):
    """
        API end-point for ConsumptionRecordLine model
    """
    queryset = ConsumptionRecordLine.objects.all()
    serializer_class = ConsumptionRecordLineSerializer


class IncomingShipmentViewSet(BaseModelViewSet):
    """
        API end-point for IncomingShipment model
    """
    queryset = IncomingShipment.objects.all()
    serializer_class = IncomingShipmentSerializer


class IncomingShipmentLineViewSet(BaseModelViewSet):
    """
        API end point for IncomingShipmentLine model
    """
    queryset = IncomingShipmentLine.objects.all()
    serializer_class = IncomingShipmentLineSerializer


class OutgoingShipmentViewSet(BaseModelViewSet):
    """
        API end-point for OutgoingShipment model
    """
    queryset = OutgoingShipment.objects.all()
    serializer_class = OutgoingShipmentSerializer