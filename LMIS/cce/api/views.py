"""
    cce/views.py holds the API end-point for CCE app. it is used to define the API views from which external
    clients can interact with the CCE app to perform operations such as Create, Retrieve, Update, Delete etc on the CCE
    models via ModelViewSet functions such as list(), retrieve(), update(), partial_update(), destroy() and ad-hoc
    functions can be added too.
"""

#import project modules
from core.api.views import BaseModelViewSet
from cce.models import StorageLocation, StorageLocationType, StorageLocationTempLog, StorageLocationProblemLog
from .serializers import (StorageLocationSerializer, StorageLocationTypeSerializer, StorageLocationTempLogSerializer,
                          StorageLocationProblemLogSerializer)


class StorageLocationViewSet(BaseModelViewSet):
    """
        REST API end-point for CCE that allows CRUD operations etc to be performed on StorageLocation models via
        REST url
    """
    queryset = StorageLocation.objects.all()
    serializer_class = StorageLocationSerializer


class StorageLocationTypeViewSet(BaseModelViewSet):
    """
        REST API end-point for StorageLocationType that allows CRUD operations etc to be performed on
        StorageLocationType models via REST API URL
    """
    queryset = StorageLocationType.objects.all()
    serializer_class = StorageLocationTypeSerializer


class StorageLocationTempLogViewSet(BaseModelViewSet):
    """
        REST API end-point for StorageLocationTempLog that allows CRUD operations etc to be performed on
        StorageLocationTempLog models via REST API URL
    """
    queryset = StorageLocationTempLog.objects.all()
    serializer_class = StorageLocationTempLogSerializer


class StorageLocationProblemLogViewSet(BaseModelViewSet):
    """
        REST API end-point for StorageLocationProblemLog that allows CRUD operations etc to be performed on
        StorageLocationProblemLog models via REST API URL
    """
    queryset = StorageLocationProblemLog.objects.all()
    serializer_class = StorageLocationProblemLogSerializer