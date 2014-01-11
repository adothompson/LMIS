"""
    facilities/views.py holds the API end-point for Facility and its related models. it is used to define the API views
    from which external clients can interact with the models to perform operations such as Create, Retrieve, Update,
    Delete etc via ModelViewSet functions such as list(), retrieve(), update(), partial_update(), destroy() and
    ad-hoc functions can be added too.
"""

#import LMIS project modules
from core.api.views import BaseModelViewSet
from facilities.models import (Facility, FacilityType, FacilitySupportedProgram, FacilitySupportedProgramProduct,
                     SupervisoryNode, OrderGroup, Warehouse, WarehouseType)

from facilities.api.serializers import (FacilitySerializer, FacilityTypeSerializer, WarehouseSerializer,
                                        FacilitySupportedProgramProductSerializer, SupervisoryNodeSerializer,
                                        OrderGroupSerializer, FacilitySupportedProgramSerializer,
                                        WarehouseTypeSerializer)


class FacilityTypeViewSet(BaseModelViewSet):
    """
        API end-point for FacilityType model.
    """
    queryset = FacilityType.objects.all()
    serializer_class = FacilityTypeSerializer


class FacilityViewSet(BaseModelViewSet):
    """
        API end-point for Facility model
    """
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class FacilitySupportedProgramProductViewSet(BaseModelViewSet):
    """
        API end-point for FacilitySupportedProgramProduct model
    """
    queryset = FacilitySupportedProgramProduct.objects.all()
    serializer_class = FacilitySupportedProgramProductSerializer


class SupervisoryNodeViewSet(BaseModelViewSet):
    """
        API end-point for SupervisoryNode model
    """
    queryset = SupervisoryNode.objects.all()
    serializer_class = SupervisoryNodeSerializer


class OrderGroupViewSet(BaseModelViewSet):
    """
        API end-point for OrderGroup model
    """
    queryset = OrderGroup.objects.all()
    serializer_class = OrderGroupSerializer


class FacilitySupportedProgramViewSet(BaseModelViewSet):
    """
        API end-point for FacilitySupportedProgram model
    """
    queryset = FacilitySupportedProgram.objects.all()
    serializer_class = FacilitySupportedProgramSerializer


class WarehouseTypeViewSet(BaseModelViewSet):
    """
        API end-point for WarehouseType model
    """
    queryset = WarehouseType.objects.all()
    serializer_class = WarehouseTypeSerializer


class WarehouseViewSet(BaseModelViewSet):
    """
        API end-point for Warehouse model
    """
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer