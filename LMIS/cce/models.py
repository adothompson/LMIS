"""
    This module handles all cold chain equipment management issues such as temperature log, problem log, current
    facility the CCE is at and the warehouse.
"""

#import django modules
from django.db import models

#import external modules
import reversion
from mptt.models import MPTTModel, TreeForeignKey
from model_utils import Choices

#import project app modules
from core.models import BaseModel, UnitOfMeasurement
from facilities.models import Facility


class StorageLocationType(MPTTModel, BaseModel):
    """
       StorageLocationType is used to group storage locations both cold and dry storage location
    """
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='sub_types')

    def __str__(self):
        return '{name}'.format(name=self.name)


class StorageLocation(MPTTModel, BaseModel):
    """
        StorageLocation is used to model physical or virtual places where products are stored
    """
    STATUS = Choices((0, 'working', ('Working')), (1, 'not_working', ('Not Working')), (2, 'in_repair', ('In Repair')),)
    code = models.CharField(max_length=55, unique=True)
    name = models.CharField(max_length=55, unique=True)
    facility = models.ForeignKey(Facility)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children_storage_location')
    gross_capacity = models.FloatField(blank=True, null=True)
    net_capacity = models.FloatField(blank=True, null=True)
    capacity_uom = models.ForeignKey(UnitOfMeasurement, related_name='capacity_uom', null=True, blank=True)
    type = models.ForeignKey(StorageLocationType)
    is_cold_store = models.BooleanField()
    minimum_temperature = models.FloatField(blank=True, null=True, verbose_name='min_temp.')
    maximum_temperature = models.FloatField(blank=True, null=True, verbose_name='max_temp.')
    temperature_uom = models.ForeignKey(UnitOfMeasurement, related_name='temp_uom', blank=True, null=True)
    status = models.IntegerField(choices=STATUS)

    def __str__(self):
        return '{code}-{name}'.format(code=self.code, name=self.name)


class StorageLocationTempLog(BaseModel):
    """
        Used to keep storage locations' Temp. Log especially cold chain types
    """
    temperature = models.FloatField()
    temperature_uom = models.ForeignKey(UnitOfMeasurement)
    storage_location = models.ForeignKey(StorageLocation)
    date_time_logged = models.DateTimeField()

    def __str__(self):
        return '{storage_loc_code}-{temp}'.format(storage_loc_code=self.storage_location.code, temp=self.temperature)


class StorageLocationProblemLog(BaseModel):
    """
        This model is used to keep problem log for storage locations
    """
    storage_location = models.ForeignKey(StorageLocation)
    description = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    fixed_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{storage_loc_name}-{description}'.format(storage_loc_code=self.storage_location.name,
                                                         description=self.description)


#Register models that will be tracked with reversion
reversion.register(StorageLocationType)
reversion.register(StorageLocation)
reversion.register(StorageLocationTempLog)
reversion.register(StorageLocationProblemLog)