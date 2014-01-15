from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


from .serializers import ProgramSerializer, ProgramProductSerializer, ProgramProductAllocationInfoSerializer
from .models import Program, ProgramProduct, ProgramProductAllocationInfo


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramProductListViewSet(viewsets.ModelViewSet):
    queryset = ProgramProduct.objects.all()
    serializer_class = ProgramProductSerializer


class ProgramProductAllocationInfoViewSet(viewsets.ModelViewSet):
    queryset = ProgramProductAllocationInfo.objects.all()
    serializer_class = ProgramProductAllocationInfoSerializer
