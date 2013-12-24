"""
    CORE module holds core models that are used throughout the LMIS project.
"""

#import django modules
from django.db import models
from django.contrib.auth.models import User

#import external modules
from mptt.models import MPTTModel, TreeForeignKey


class BaseModel(models.Model):
    """
        BaseModel is the abstract base class for all the LMIS domain models.
    """
    #created_by = models.ForeignKey('User', blank=True, null=True, related_name='%(app_label)s_%(class)s_created_by')
    #modified_by = models.ForeignKey('User', blank=True, null=True, related_name='%(app_label)s_%(class)s_modified_by')
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)


class UOMCategory(MPTTModel, BaseModel):
    """
        This represents categories of different unit of measurements.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='sub_uom_categories')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


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
            symbol_position_before: this is used to know how to format this currency, default is True hence currency symbol
            appear before the monetary value.
    """
    SYMBOL_BEFORE = 1
    SYMBOL_AFTER = 1
    SYMBOL_POSITIONS = (
        (SYMBOL_BEFORE, 'Before'),
        (SYMBOL_AFTER, 'After'),
    )
    name = models.CharField(max_length=35, unique=True)
    symbol = models.CharField(max_length=5, unique=True)
    code = models.CharField(max_length=15, unique=True)
    symbol_position_before = models.IntegerField(max_length=1, choices=SYMBOL_POSITIONS, default=SYMBOL_BEFORE)

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
            subdivision :  holds PyCountry Subdivision unique code for the subdivision. subdivision could be a region
                or state, it varies from one country to another.
            country : This is used to hold the country code.
    """
    tag = models.CharField(max_length=35, blank=True, null=True)
    street = models.CharField(max_length=35, blank=True, null=True)
    zip = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    #ward = models.ForeignKey('Ward', blank=True, null=True)
    #lga = models.ForeignKey('LGA', blank=True, null=True)
    subdivision = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return '{street}'.format(street=self.streets)

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

    class Meta:
        app_label = 'core'


class Manufacturer(Party):
    """
        This models product manufacturers and each manufacturer can have 0 or more products that it supplies and
        a product can have one or more manufacturers.
    """
    products = models.ManyToManyField('Product', blank=True, null=True)


class Company(Party):
    """
        Base class for Facilities, Partners,  etc,
    """
    header = models.CharField(max_length=100, blank=True, null=True)
    footer = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'core'

    def __str__(self):
        return '{name}'.format(name=self.name)


class CompanyCategory(MPTTModel, BaseModel):
    """
        Used to model company category, it can be Facility, Manufacturer, Partner, FacilityOperators etc.
    """
    name = models.CharField(max_length=35, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='sub_company_categories')

    def __str__(self):
        return '{name}'.format(name=self.name)

    class MPTTMeta:
        app_label = 'core'


class EmployeeCategory(MPTTModel, BaseModel):
    """
        used to model employee categories
    """
    name = models.CharField(max_length=35, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='sub_employee_categories')

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
    main_company = models.ForeignKey(Company, related_name="main_company_employees", blank=True, null=True)
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
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=200, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='sub_facility_types')
    #TODO: find out what nominal max month means.
    #level_id = models.IntegerField()
    #nominal_max_month = models.IntegerField()
    #nominal_eop = models.FloatField(blank=True, null=True)
    active = models.BooleanField()

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class FacilityTypeApprovedProduct(BaseModel):
    """
        Used to represent the program products that are approved for a given facility type.
    """
    facility_type = models.ForeignKey(FacilityType)
    program_product = models.ForeignKey('ProgramProduct')
    max_months_of_stock = models.IntegerField()

    class Meta:
        app_label = 'core'


class Facility(MPTTModel, Company):
    """
        This is used to model stores, health facilities, Satellite stores etc
        facility_operator is a set of organizations that
    """
    description = models.CharField(max_length=200, blank=True)
    facility_operators = models.ForeignKey(Company, verbose_name='facility operators')
    global_location_no = models.CharField(max_length=55, blank=True)
    #TODO: this will be replaced by the location module. geo_zone = models.ForeignKey(GeographicZone)
    facility_type = models.ForeignKey(FacilityType)
    catchment_population = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    operated_by = models.ManyToManyField('FacilityOperator', blank=True, null=True)
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

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class WarehouseType(BaseModel):
    """
        This is used to model different types of Warehouse or Storage Location. it can be a Physical Warehouse,
        In-Transit Warehouse(like products being transported)
    """
    code = models.ForeignKey(max_length=35, unique=True)
    name = models.ForeignKey(max_length=55, unique=True)
    description = models.CharField(max_length=100, blank=True)


class Warehouse(BaseModel):
    """
        This defines the storage locations at each Facility. a facility can have more than one warehouse i.e storage -
        location.
    """
    code = models.CharField(max_length=55, unique=True)
    facility = models.ForeignKey(Facility)
    is_refrigerated = models.BooleanField(default=True, verbose_name='cold storage warehouse')
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    cold_storage_gross_capacity = models.FloatField(blank=True, null=True)
    cold_storage_net_capacity = models.FloatField(blank=True, null=True)
    ambient_storage_gross_capacity = models.FloatField(blank=True, null=True)
    ambient_storage_net_capacity = models.FloatField(blank=True, null=True)


class Program(BaseModel):
    """
        Program is used to represent different types of health programs that facilities runs. ARV, HIV, KIck Polio
    """
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=55, blank=True)
    active = models.BooleanField()
    push = models.BooleanField()

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class ProgramProduct(BaseModel):
    """
        ProgramProduct models set of products that can be used in a Program.
        it is recorded for each product used in a program
    """
    program = models.ForeignKey(Program)
    product = models.ForeignKey(Product)
    doses_per_month = models.IntegerField()
    is_active = models.BooleanField()
    current_price = models.DecimalField(max_digits=21, decimal_places=2)
    program_product_info = models.OneToOneField(ProgramProductOrderInfo)
    program_product_price = models.ForeignKey(ProgramProductPrice)

    def __str__(self):
        return '{program}-{product}'.format(program=self.program.name, product=self.product.name)

    class Meta:
        app_label = 'core'


class ProgramProductPrice(BaseModel):
    """
        ProgramProductPrice is used to model the changes in price of each program product,
        start date and end date represents the period which the price was valid.
    """
    price_per_dosage = models.DecimalField(max_digits=21, decimal_places=2)
    price_currency = models.ForeignKey(Currency, blank=True, null=True)
    funding_source = models.ManyToManyField(Company)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        app_label = 'core'


class FacilityProgramSupported(BaseModel):
    """
        This is used to model programs that a facility supports. its is entered for each program a facility supports.
        and indicates the status of the program at each facility start date and end date.
    """
    program = models.ForeignKey(Program)
    facility = models.ForeignKey(Facility)
    active = models.BooleanField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        app_label = 'core'


class ProgramProductOrderInfo(BaseModel):
    """
        ProgramProductOrderInfo is used for holding allocation and order point information for each program product.
    """
    who_ratio = models.FloatField()
    doses_per_year = models.IntegerField()
    wastage_factor = models.FloatField()
    buffer_percentage = models.FloatField()
    minimum_value = models.IntegerField()
    maximum_value = models.IntegerField()
    adjustment_value = models.IntegerField()

    class Meta:
        app_label = 'core'


class SupervisoryNode(MPTTModel, BaseModel):
    """
        SupervisoryNode is a facility that supervises and manages a OrderGroup, it has a hierarchical
        structure. This can be used to know whom to escalate notification or alert to.
    """
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=55, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='parent_supervisory_node')
    facility = models.ForeignKey(Facility)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class OrderGroup(BaseModel):
    """
        OrderGroup is used to model facilities that has same supervisory node or
         makes order from same supplying facility
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
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=35)




