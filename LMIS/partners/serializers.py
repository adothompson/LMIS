from rest_framework import serializers


from .models import Program, ProgramProduct, ProgramProductAllocationInfo
from core.api.serializers import BaseModelSerializer


class ProgramSerializer(BaseModelSerializer):
    class Meta:
        model = Program


class ProgramProductSerializer(BaseModelSerializer):
    class Meta:
        model = ProgramProduct


class ProgramProductAllocationInfoSerializer(BaseModelSerializer):
    class Meta:
        model = ProgramProductAllocationInfo