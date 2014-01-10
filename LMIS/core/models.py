"""
    CORE module holds core models that are used throughout the LMIS project.
"""

#import django modules
from django.db import models
from django.contrib.auth.models import User

#import external modules
import reversion
from mptt.models import MPTTModel, TreeForeignKey
from django_extensions.db.fields import UUIDField
from model_utils.models import TimeStampedModel
from model_utils import Choices

#import project app modules
#from locations.models import Location


class BaseModel(TimeStampedModel):
    """
        BaseModel is the abstract base class for all the LMIS domain models. it is used to keep track of who created
        an object and when and when last an object was modified.
        it extends TimeStampedModel which adds self-updating created and modified fields on any model that
        inherits from it.

    """
    uuid = UUIDField(version=4, primary_key=True)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='%(app_label)s_%(class)s_created_by')
    modified_by = models.ForeignKey(User, blank=True, null=True,
                                    related_name='%(app_label)s_%(class)s_modified_by')

    class Meta:
        abstract = True


class VVMStage(BaseModel):
    """
        This is used to represent possible stages of vaccine vial monitor attached to vaccines to  which gives a visual
        indication of whether the vaccine has been kept at a temperature which preserves its potency.
    """
    STAGES = Choices('Stage 1', 'Stage 2', 'Stage 3', 'Stage 4')

    class Meta:
        managed = False


class UOMCategory(MPTTModel, BaseModel):
    """
        This represents categories of different unit of measurements.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='%(app_label)s_%(class)s_sub_uom_categories')

    def __str__(self):
        return '{name}'.format(name=self.name)

    class MPTTMeta:
        order_insertion_by = ['name']


class UnitOfMeasurement(BaseModel):
    """
        This represents the standard of unit of measurement of things like temp, volume, dosage etc etc.
    """
    name = models.CharField(max_length=25, unique=True)
    symbol = models.CharField(max_length=10)
    uom_category = models.ForeignKey(UOMCategory)
    rate = models.FloatField(null=True, blank=True)
    factor = models.FloatField(null=True, blank=True)
    rounding_precision = models.IntegerField(max_length=2, blank=True, null=True)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class Rate(BaseModel):
    """
        This belongs to the currency class and is used to model different exchange rates for the currency.
        a currency should have at least one rate with value equals to 1, this is the rate of the currency against itself
        The date is the date from which the rate becomes effective.
    """
    name = models.CharField(max_length=35)
    value = models.DecimalField(max_digits=21, decimal_places=2)
    date = models.DateField(null=True, blank=True, verbose_name='effective date')
    currency = models.ForeignKey('Currency')

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class Currency(BaseModel):
    """
        This is used to represent currency for monetary units

        Attribute:
            symbol_position_before: this is used to know how to format this currency, default is True hence currency
            symbol appear before the monetary value.
            name: Dollars
            symbol: $
            code: USD
    """
    SYMBOL_POSITION = Choices('before', 'after')
    name = models.CharField(max_length=35, unique=True)
    symbol = models.CharField(max_length=5, unique=True)
    code = models.CharField(max_length=15, unique=True)
    symbol_position = models.CharField(choices=SYMBOL_POSITION, default=SYMBOL_POSITION.before, max_length=20)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class Contact(BaseModel):
    """
        This models contact info of other domain models such as Facility, Partners, Manufacturers etc
    """
    tag = models.CharField(max_length=35, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    fax = models.CharField(max_length=35, blank=True)
    website = models.URLField(blank=True)
    skype = models.CharField(max_length=35, blank=True)
    mobile = models.CharField(max_length=15, blank=True)
    sip = models.CharField(max_length=25, blank=True)
    irc = models.CharField(max_length=35, blank=True)
    jabber = models.CharField(max_length=35, blank=True)
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return '{tag}'.format(tag=self.tag)

    class Meta:
        app_label = 'core'


class Address(BaseModel):
    """
        Attributes:
            tag : used to refer to the address, could be Head Office Address, Branch Office Address, etc
            country : This is used to hold the country code.
    """
    tag = models.CharField(max_length=35, blank=True, null=True)
    street = models.CharField(max_length=35, blank=True, null=True)
    zip = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    subdivision = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return '{street}'.format(street=self.street)

    class Meta:
        app_label = 'core'


class Party(BaseModel):
    """
        This is the abstract base class of all entities such as Employee, Facility, Partners, Manufacturers
    """
    name = models.CharField(max_length=55, unique=True)
    code = models.CharField(max_length=35, unique=True)
    contact = models.ForeignKey(Contact, null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True)

    class Meta:
        abstract = True
        app_label = 'core'


class Company(Party):
    """
        Base class for Facility. Company is also used to model Manufacturers, Suppliers, Partners etc,  etc,
    """
    products = models.ManyToManyField('Product', blank=True, null=True)
    header = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey('CompanyCategory')
    footer = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class CompanyCategory(MPTTModel, BaseModel):
    """
        Used to model company category, it can be Facility, Partner, FacilityOperators etc.
    """
    name = models.CharField(max_length=35, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='%(app_label)s_%(class)s_sub_company_categories')

    def __str__(self):
        return '{name}'.format(name=self.name)

    class MPTTMeta:
        app_label = 'core'


class EmployeeCategory(MPTTModel, BaseModel):
    """
        used to model employee categories
    """
    name = models.CharField(max_length=35, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='%(app_label)s_%(class)s_sub_employee_categories')

    def __str__(self):
        return '{name}'.format(name=self.name)

    class MPTTMeta:
        order_insertion_by = ['name']
        app_label = 'core'


class Employee(Party):
    """
        This represents Employees of company's and stores, an employee could also be users of the system, if it has
        User attribute.

        Attributes:
        current_company: The company field defines the current company of the user
        main_company: The main company define which current company a user can choose: either the main company itself
            or one of the children companies.
    """
    current_company = models.ForeignKey(Company, related_name="employees")
    main_company = models.ForeignKey(Company,
                                     related_name="%(app_label)s_%(class)s_main_company_employees", blank=True,
                                     null=True)
    category = models.ForeignKey(EmployeeCategory)
    user = models.OneToOneField(User, blank=True, null=True)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


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

    class Meta:
        app_label = 'core'

#TODO: remove if not necessary
# class FacilityTypeApprovedProgramProduct(BaseModel):
#     """
#         Used to represent the program products that are approved for a given facility type.
#     """
#     facility_type = models.ForeignKey(FacilityType)
#     program_product = models.ForeignKey('ProgramProduct')
#     max_months_of_stock = models.IntegerField(blank=True, null=True)
#
#     def __str__(self):
#         return '{name}'.format(name=self.name)
#
#     class Meta:
#         app_label = 'core'


class Facility(MPTTModel, Company):
    """
        This is used to model stores, health facilities, Satellite stores etc
        facility_operator is a set of organizations that
    """
    description = models.CharField(max_length=55, blank=True)
    facility_type = models.ForeignKey(FacilityType)
    supplies_others = models.BooleanField()
    sdp = models.BooleanField(verbose_name="is service delivery point")
    facility_operators = models.ManyToManyField(Company, blank=True, null=True, related_name='facility_operators')
    global_location_no = models.CharField(max_length=55, blank=True)
    catchment_population = models.IntegerField(blank=True, null=True)
    #location = models.ForeignKey(Location, null=True)
    has_electricity = models.NullBooleanField(blank=True)
    is_online = models.NullBooleanField(blank=True, null=True)
    has_electronic_scc = models.NullBooleanField(blank=True, null=False)
    has_electronic_dar = models.NullBooleanField(blank=True, null=False)
    is_active = models.NullBooleanField(default=True)
    go_live_date = models.DateField()
    go_down_date = models.DateField(blank=True, null=True)
    is_satellite = models.NullBooleanField(blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='child_facilities')
    virtual_facility = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class WarehouseType(BaseModel):
    """
        This is used to model different types of Warehouse or Storage Location. it can be a Physical Warehouse,
        In-Transit Warehouse(like products being transported)
    """
    #code = models.CharField(max_length=35, unique=True)
    #name = models.CharField(max_length=55, unique=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


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

    class Meta:
        app_label = 'core'


class Program(BaseModel):
    """
        Program is used to represent different types of health programs that facilities runs. ARV, HIV, KIck Polio
    """
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=55, blank=True)
    active = models.BooleanField()
    partners = models.ManyToManyField(Company)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class ProgramProductAllocationInfo(BaseModel):
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
    adjustment_value = models.IntegerField()

    class Meta:
        app_label = 'core'


class ProgramProduct(BaseModel):
    """
        ProgramProduct models set of products that can be used in a Program.
        it is recorded for each product used in a program

        -unit_per_target is the number of base units of the product required per person(in the target population)
         to complete treatment or immunization.
    """
    program = models.ForeignKey(Program)
    product = models.ForeignKey('Product')
    unit_per_target = models.IntegerField()
    current_price_per_unit = models.DecimalField(max_digits=21, decimal_places=2, verbose_name='price per uom')
    price_currency = models.ForeignKey(Currency, blank=True, null=True)
    funding_source = models.ManyToManyField(Company)
    is_active = models.BooleanField()

    def __str__(self):
        return '{program}-{product}'.format(program=self.program.name, product=self.product.name)

    class Meta:
        app_label = 'core'


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

    class Meta:
        app_label = 'core'


class FacilitySupportedProgramProduct(BaseModel):
    """
        This is used to keep track of program-products a facility support, how the product is allocated to the facility
        , who supplies the facility the product, current status of the program product at the facility etc.
    """
    facility = models.ForeignKey(Facility)
    program_product = models.ForeignKey(ProgramProduct)
    allocation_info = models.OneToOneField(ProgramProductAllocationInfo)
    active = models.BooleanField(default=True)
    order_group = models.ForeignKey('OrderGroup')

    class Meta:
        app_label = 'core'


class SupervisoryNode(MPTTModel, BaseModel):
    """
        SupervisoryNode is a facility that supervises and manages an OrderGroup, it has a hierarchical
        structure. This can be used to know whom to send escalated notification or alert to.
    """
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=55, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='parent_supervisory_node')
    facility = models.ForeignKey(Facility)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


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
    member_facilities = models.ManyToManyField(Facility, blank=True, null=True, verbose_name='member facilities')

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class ProcessingPeriod(BaseModel):
    """
        Used to model start and end date of processing or carrying out an action.
    """
    name = models.CharField(max_length=35, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class ProductCategory(MPTTModel, BaseModel):
    """
       This is used group products, it is hierarchical. it can be device, vaccine, diluent, syringes etc
    """
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='sub_product_categories')

    def __str__(self):
        return '{name}'.format(name=self.name)

    class MPTTMeta:
        order_insertion_by = ['name']
        app_label = 'core'


class Product(BaseModel):
    """
        Product represents a particular object that is used in a program, e.g BCG, OPV, etc.

        -active: can be used to disable a product if false.
    """
    code = models.CharField(max_length=35, unique=True)
    name = models.CharField(max_length=55, unique=True)
    category = models.ForeignKey(ProductCategory, verbose_name='product category')
    base_uom = models.ForeignKey(UnitOfMeasurement, verbose_name='default unit of measurement')
    description = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class ProductPresentation(BaseModel):
    """
        This is used to model presentation of a product,
        -it can be 20 uom where uom is doses per vial for vaccines,
        -it can be 5 uom where uom is unit per box for syringes

    """
    code = models.CharField(max_length=35, unique=True)
    name = models.CharField(max_length=55, unique=True)
    value = models.IntegerField()
    uom = models.ForeignKey(UnitOfMeasurement, verbose_name='presentation unit of measurement')
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class ModeOfAdministration(BaseModel):
    """
        This models how a product is used. it could be Oral, Subcutaneous, Intramuscular for Vaccine or
        N/A (Not Applicable) for some device that doesnt have mode of administration.
        for vaccines that can be delivered as SC or IM, Mode of Administration can be used to model that too.
        e.g code for IM and SC mode of admin can be IM-SC
    """
    code = models.CharField(max_length=35)
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class ProductItem(BaseModel):
    """
        ProductItem is used to describe a particular product in stock inventory listing. It is used to uniquely
        identify collection of a given product that has same value for a given set of attributes that can vary from
         one collection of same product to another.

         for instance a collection of a product with same value for each of ProductItem attributes will have same
         product item code.
    """
    code = models.CharField(max_length=35, unique=True)
    name = models.CharField(max_length=55, unique=True)
    product = models.ForeignKey(Product)
    presentation = models.ForeignKey('ProductPresentation')
    manufacturer = models.ForeignKey(Company)
    product_batch_no = models.CharField(max_length=35)
    moh_bar_code = models.CharField(max_length=255, blank=True)
    gtin = models.CharField(max_length=35, blank=True)
    price_per_unit = models.DecimalField(max_digits=21, decimal_places=2)
    price_currency = models.ForeignKey(Currency, blank=True, null=True)
    expiration_date = models.DateField()
    country_of_origin = models.CharField(max_length=55)
    mode_of_use = models.ForeignKey('ModeOfAdministration', blank=True, null=True)
    description = models.CharField(max_length=100, blank=True)
    weight_per_unit = models.FloatField(max_length=21, blank=True, null=True)
    weight_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True, related_name='product_item_weight_uom')
    volume_per_unit = models.FloatField(blank=True, null=True)
    volume_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True, related_name='product_item_volume_uom')
    active = models.BooleanField()

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


#register models to be tracked via Reversion

reversion.register(UOMCategory)
reversion.register(UnitOfMeasurement)
reversion.register(Rate)
reversion.register(Currency)
reversion.register(Contact)
reversion.register(Address)
reversion.register(Company)
reversion.register(CompanyCategory)
reversion.register(EmployeeCategory)
reversion.register(Employee)
reversion.register(FacilityType)
reversion.register(Facility)
reversion.register(WarehouseType)
reversion.register(Warehouse)
reversion.register(Program)
reversion.register(ProgramProductAllocationInfo)
reversion.register(FacilitySupportedProgram)
reversion.register(FacilitySupportedProgramProduct)
reversion.register(SupervisoryNode)
reversion.register(OrderGroup)
reversion.register(ProcessingPeriod)
reversion.register(ProductCategory)
reversion.register(Product)
reversion.register(ProductPresentation)
reversion.register(ModeOfAdministration)
reversion.register(ProductItem)

