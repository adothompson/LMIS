"""
    Facility models.py holds facility related models
"""

#import core django modules
from django.db import models

#import external modules
import reversion
from mptt.models import MPTTModel, TreeForeignKey


#import project app modules
from locations.models import Location
from core.models import BaseModel, Company
from partners.models import ProgramProduct, Program


class FacilityType(MPTTModel, BaseModel):
    """
        This models different types of facilities, each country should have their different types of facilities.
    """
    code = models.CharField(max_length=35, unique=True)
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=55, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='sub_facility_types')
    active = models.BooleanField()

    def __str__(self):
        return '{name}'.format(name=self.name)


class Facility(MPTTModel, Company):
    """
        This is used to model stores, health facilities, Satellite stores etc
        facility_operator is a set of organizations that
    """
    description = models.CharField(max_length=55, blank=True)
    facility_type = models.ForeignKey(FacilityType)
    supplies_others = models.BooleanField()
    is_sdp = models.BooleanField(verbose_name="is service delivery point")
    facility_operators = models.ManyToManyField(Company, blank=True, null=True, related_name='facility_operators')
    global_location_no = models.CharField(max_length=55, blank=True)
    catchment_population = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location)
    has_electricity = models.BooleanField()
    is_online = models.BooleanField()
    has_electronic_scc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    go_live_date = models.DateField()
    go_down_date = models.DateField(blank=True, null=True)
    is_satellite = models.BooleanField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='child_facilities')
    virtual_facility = models.BooleanField()

    def __str__(self):
        return '{name}'.format(name=self.name)


class WarehouseType(BaseModel):
    """
        This is used to model different types of Warehouse or Storage Location. it can be a Physical Warehouse,
        In-Transit Warehouse(like products being transported)
    """
    code = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{code}'.format(code=self.code)


class Warehouse(BaseModel):
    """
        This defines the storage locations at each Facility. a facility can have more than one warehouse i.e storage -
        location.
    """
    code = models.CharField(max_length=55, unique=True)
    facility = models.ForeignKey(Facility)
    is_refrigerated = models.BooleanField(default=False, verbose_name='is cold storage warehouse')
    cold_storage_gross_capacity = models.FloatField(blank=True, null=True)
    cold_storage_net_capacity = models.FloatField(blank=True, null=True)
    ambient_storage_gross_capacity = models.FloatField(blank=True, null=True)
    ambient_storage_net_capacity = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '{name}'.format(name=self.name)


class FacilitySupportedProgram(BaseModel):
    """
        This is used to model programs that a facility supports. its is entered for each program a facility supports.
        and indicates the status(active or not) of the program at each facility, program start date and end date at the
        facility.
    """
    program = models.ForeignKey(Program)
    facility = models.ForeignKey(Facility)
    active = models.BooleanField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)


class FacilityProgramProductParameter(BaseModel):
    """
        This models information used to allocate a program product to a facility.
    """
    #World Health Ratio for the program
    who_ratio = models.FloatField()
    coverage_rate = models.FloatField(verbose_name='coverage rate(%)')
    wastage_rate = models.FloatField(verbose_name='wastage rate(%)')
    buffer_percentage = models.FloatField()
    target_population = models.IntegerField(verbose_name='target population(%)')
    min_quantity = models.IntegerField()
    max_quantity = models.IntegerField()
    push = models.BooleanField()
    lead_time = models.IntegerField(verbose_name='lead time(weeks)')
    #supply_interval is specified in months
    supply_interval = models.IntegerField(verbose_name='supply interval(months)')


class FacilitySupportedProgramProduct(BaseModel):
    """
        This is used to keep track of program-products a facility support, how the product is allocated to the facility
        , who supplies the facility the product, current status of the program product at the facility etc.
    """
    facility = models.ForeignKey(Facility)
    program_product = models.ForeignKey(ProgramProduct)
    allocation_info = models.OneToOneField(FacilityProgramProductParameter)
    active = models.BooleanField(default=True)
    order_group = models.ForeignKey('OrderGroup')


class SupervisoryNode(MPTTModel, BaseModel):
    """
        SupervisoryNode is a facility that supervises and manages an OrderGroup, it has a hierarchical
        structure. This can be used to know whom to send escalated notification or alert to.
    """
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=55, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='supervised_nodes')
    facility = models.ForeignKey(Facility)

    def __str__(self):
        return '{name}'.format(name=self.name)


class OrderGroup(BaseModel):
    """
        OrderGroup is used to link a Supplying Facility to other facility which they can supply items and
        the supervisory nodes for the order group.
        A facility can belong to more than one order group and an order group can have more than one facility.

        A facility can link one of its order groups as the supplier of a program product it supports.
    """
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=55, blank=True)
    supervisory_node = models.ForeignKey('SupervisoryNode')
    member_facilities = models.ManyToManyField(Facility, blank=True, null=True, verbose_name='member_facilities')

    def __str__(self):
        return '{name}'.format(name=self.name)


reversion.register(FacilityType)
reversion.register(Facility)
reversion.register(WarehouseType)
reversion.register(Warehouse)
reversion.register(FacilityProgramProductParameter)
reversion.register(FacilitySupportedProgram)
reversion.register(FacilitySupportedProgramProduct)
reversion.register(SupervisoryNode)
reversion.register(OrderGroup)