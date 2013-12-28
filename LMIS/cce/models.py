#import django modules
from django.db import models

#import external modules
from django_extensions.db.fields import UUIDField

#import project app modules
from core.models import BaseModel, UnitOfMeasurement, Facility, Warehouse


class ColdChainEquipmentType(BaseModel):
    """
        This class is used to classify different types of ColdChainEquipment such as Freezers and Fridge etc
        Fridge has minimum of +2 degree celsius to +8 degree celsius.
    """
    uuid = UUIDField(version=4, primary_key=True)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20, unique=True)
    minimum_temperature = models.FloatField(blank=True, null=True, verbose_name='min temp.')
    maximum_temperature = models.FloatField(blank=True, null=True, verbose_name='max temp.')
    temperature_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True)

    def __str__(self):
        return '{name}'.format(name=self.name)


class ColdChainEquipment(BaseModel):
    """
        Cold Chain Equipment is used to store vaccines in order to avoid cold chain breach, could be freezer, fridge,
        insulated coolers etc.
    """
    uuid = UUIDField(version=4, primary_key=True)
    #TODO: model status with django model util
    CCE_STATUS = ((0, "Good Working Condition"), (1, "Faulty"), (2, "Not Working"))
    code = models.CharField(max_length=35, unique=True)
    gross_capacity = models.FloatField(blank=True, null=True)
    net_capacity = models.FloatField(blank=True, null=True)
    capacity_uom = models.ForeignKey(UnitOfMeasurement, null=True, blank=True)
    cce_type = models.ForeignKey(ColdChainEquipmentType)
    cce_status = models.IntegerField(default=0, choices=CCE_STATUS)
    facility = models.ForeignKey(Facility)
    storage_location = models.ForeignKey(Warehouse, blank=True, null=True)

    def __str__(self):
        return '{code}'.format(code=self.code)


class CCETemperatureLog(BaseModel):
    """
        Used to keep log or CCE temperature readings
    """
    uuid = UUIDField(version=4, primary_key=True)
    temperature = models.FloatField()
    temperature_uom = models.ForeignKey(UnitOfMeasurement)
    cce = models.ForeignKey(ColdChainEquipment)
    date_time_logged = models.DateTimeField()

    def __str__(self):
        return '{temp} {uom_symbol}'.format(temp=self.temperature, uom_symbol=self.temperature_uom.symbol)


class CCEProblemLog(BaseModel):
    """
        This models the problem log for CCEs
    """
    uuid = UUIDField(version=4, primary_key=True)
    name = models.CharField(max_length=35)
    cce = models.ForeignKey(ColdChainEquipment)
    description = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{name}'.format(name=self.name)