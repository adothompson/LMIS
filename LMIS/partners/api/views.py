from .serializers import ProgramSerializer, ProgramProductSerializer, ProgramProductAllocationInfoSerializer
from partners.models import Program, ProgramProduct, ProgramProductAllocationInfo
from core.api.views import BaseModelViewSet


class ProgramViewSet(BaseModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramProductViewSet(BaseModelViewSet):
    queryset = ProgramProduct.objects.all()
    serializer_class = ProgramProductSerializer


class ProgramProductAllocationInfoViewSet(BaseModelViewSet):
    queryset = ProgramProductAllocationInfo.objects.all()
    serializer_class = ProgramProductAllocationInfoSerializer
