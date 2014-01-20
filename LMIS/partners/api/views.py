from .serializers import ProgramSerializer, ProgramProductSerializer
from partners.models import Program, ProgramProduct
from core.api.views import BaseModelViewSet


class ProgramViewSet(BaseModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramProductViewSet(BaseModelViewSet):
    queryset = ProgramProduct.objects.all()
    serializer_class = ProgramProductSerializer
