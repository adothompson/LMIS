"""
    core/api/serializers.py is the module for core model api data serializers
"""

#import LMIS project module
from core.api.serializers import BaseModelSerializer
from facilities.models import FacilityType, Facility, FacilitySupportedProgram


class FacilityTypeSerializer(BaseModelSerializer):
    """
        REST API serializer for FacilityType model
    """
    class Meta:
        model = FacilityType


class FacilitySerializer(BaseModelSerializer):
    """
        REST API serializer for Facility model
    """
    class Meta:
        model = Facility


class FacilitySupportedProgramSerializer(BaseModelSerializer):
    """
        REST API serializer for FacilitySupportedProgram model
    """
    class Meta:
        model = FacilitySupportedProgram
