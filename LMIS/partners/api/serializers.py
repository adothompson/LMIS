from rest_framework import serializers


from partners.models import Program, ProgramProduct
from core.api.serializers import BaseModelSerializer


class ProgramSerializer(BaseModelSerializer):
    class Meta:
        model = Program


class ProgramProductSerializer(BaseModelSerializer):
    class Meta:
        model = ProgramProduct
