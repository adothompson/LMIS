from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


from .serializers import ProgramSerializer, ProgramProductSerializer, ProgramProductAllocationInfoSerializer
from .models import Program, ProgramProduct, ProgramProductAllocationInfo
from core.api.views import BaseModelViewSet


class ProgramViewSet(BaseModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramProductListViewSet(BaseModelViewSet):
    queryset = ProgramProduct.objects.all()
    serializer_class = ProgramProductSerializer


class ProgramProductAllocationInfoViewSet(BaseModelViewSet):
    queryset = ProgramProductAllocationInfo.objects.all()
    serializer_class = ProgramProductAllocationInfoSerializer
