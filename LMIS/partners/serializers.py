from rest_framework import serializers


from .models import Program, ProgramProduct, ProgramProductAllocationInfo


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program


class ProgramProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramProduct


class ProgramProductAllocationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramProductAllocationInfo