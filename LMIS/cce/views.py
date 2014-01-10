"""
    cce/views.py holds the API end-point for CCE app. it is used to define the API views from which external
    clients can interact with the CCE app to perform operations such as Create, Retrieve, Update, Delete etc on the CCE
    models via ModelViewSet functions such as list(), retrieve(), update(), partial_update(), destroy() and ad-hoc
    functions can be added too.
"""

#import project modules
from core.views import BaseModelViewSet
from .models import ColdChainEquipment
from .api.serializers import CCESerializer


class CCEViewSet(BaseModelViewSet):
    """
        REST API end-point for CCE that allows CRUD operations etc to be performed on CCE models via REST url
    """
    queryset = ColdChainEquipment.objects.all()
    serializer_class = CCESerializer
