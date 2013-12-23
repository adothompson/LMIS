#import django modules
from django.db import models

#import external modules
from mptt.models import TreeForeignKey, MPTTModel

#import project app modules
from core.models import BaseModel, Company


class FacilityType(MPTTModel, BaseModel):
    """
        This models different types of facilities, each country should have their different types of facilities.
    """
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=200, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='sub_facility_types')
    #level_id = models.IntegerField()
    #TODO: i think we should model FacilityType level as as a separate Hierarchical Model using MPTT
    #nominal_max_month = models.IntegerField()
    #TODO: find out what nominal max month means.
    #nominal_eop = models.FloatField(blank=True, null=True)
    active = models.BooleanField()


class FacilityTypeApprovedProduct(BaseModel):
    """
        Used to represent the program products that are approved for a given facility type.
    """
    facility_type = models.ForeignKey(FacilityType)
    program_product = models.ForeignKey('ProgramProduct')
    max_months_of_stock = models.IntegerField()


class Facility(MPTTModel, Company):
    """
        This is used to model stores, health facilities, Satellite stores etc
    """
    description = models.CharField(max_length=200, blank=True)
    global_location_no = models.CharField(max_length=55, blank=True)
    #TODO: this will be replaced by the location module. geo_zone = models.ForeignKey(GeographicZone)
    facility_type = models.ForeignKey(FacilityType)
    catchment_population = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    operated_by = models.ManyToManyField('FacilityOperator', blank=True, null=True)
    cold_storage_gross_capacity = models.FloatField(blank=True, null=True)
    cold_storage_net_capacity = models.FloatField(blank=True, null=True)
    ambient_storage_gross_capacity = models.FloatField(blank=True, null=True)
    ambient_storage_net_capacity = models.FloatField(blank=True, null=True)
    supplies_others = models.BooleanField(default=True)
    sdp = models.BooleanField(verbose_name="is service delivery point")
    has_electricity = models.NullBooleanField(blank=True)
    is_online = models.NullBooleanField(blank=True, null=True)
    has_electronic_scc = models.NullBooleanField(blank=True, null=False)
    has_electronic_dar = models.NullBooleanField(blank=True, null=False)
    is_active = models.NullBooleanField()
    go_live_date = models.DateField()
    go_down_date = models.DateField(blank=True)
    is_satellite = models.NullBooleanField(blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='child_facilities')
    comment = models.CharField(max_length=200, blank=True)
    enabled = models.BooleanField()
    virtual_facility = models.BooleanField(default=False, blank=True)
    #TODO: uncomment when you complete implementation of ProgramSupported
    #programs_supported = models.ForeignKey('ProgramSupported',
    #                                           related_name='%(app_label)s_%(class)s_programs_supported')