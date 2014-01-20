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
from django_countries.fields import CountryField


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
    STAGES = Choices(('stage_one', 'Stage 1'), ('stage_two', 'Stage 2'), ('stage_three', 'Stage 3'),
                     ('stage_four', 'Stage 4'))

    class Meta:
        managed = False
        abstract = True


class UOMCategory(MPTTModel, BaseModel):
    """
        This represents categories of different unit of measurements.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='%(app_label)s_%(class)s_sub_uom_categories')

    class MPTTMeta:
        order_insertion_by = ['name']
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)


class UnitOfMeasurement(BaseModel):
    """
        This represents the standard of unit of measurement of things like temp, volume, dosage etc etc.
    """
    name = models.CharField(max_length=35, unique=True)
    symbol = models.CharField(max_length=25)
    uom_category = models.ForeignKey(UOMCategory)
    rate = models.FloatField(null=True, blank=True)
    factor = models.FloatField(null=True, blank=True)
    rounding_precision = models.IntegerField(max_length=2, blank=True, null=True)

    class Meta:
        app_label = 'core'
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)


class Rate(BaseModel):
    """
        This belongs to the currency class and is used to model different exchange rates for the currency.
        a currency should have at least one rate with value equals to 1, this is the rate of the currency against itself
        The date is the date from which the rate becomes effective.
    """
    name = models.CharField(max_length=35)
    value = models.DecimalField(max_digits=21, decimal_places=2)
    date = models.DateField(null=True, blank=True, verbose_name='effective date')
    currency = models.ForeignKey('Currency', related_name='rates')

    class Meta:
        app_label = 'core'
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)


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

    class Meta:
        app_label = 'core'
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)


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

    class Meta:
        app_label = 'core'
        ordering = ['tag']

    def __str__(self):
        return '{tag}'.format(tag=self.tag)


class Address(BaseModel):
    """
        Attributes:
            tag : used to refer to the address, could be Head Office Address, Branch Office Address, etc
            country : This is used to hold the country code.
    """
    tag = models.CharField(max_length=35, blank=True)
    street = models.CharField(max_length=35, blank=True)
    zip = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=35, blank=True)
    subdivision = models.CharField(max_length=10, blank=True)
    country = CountryField()

    class Meta:
        app_label = 'core'
        ordering = ['tag']

    def __str__(self):
        return '{tag}'.format(tag=self.tag)


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

    class Meta:
        app_label = 'core'
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)


class CompanyCategory(MPTTModel, BaseModel):
    """
        Used to model company category, it can be Facility, Partner, FacilityOperators etc.
    """
    name = models.CharField(max_length=35, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='%(app_label)s_%(class)s_sub_company_categories')

    class MPTTMeta:
        app_label = 'core'
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)


class EmployeeCategory(MPTTModel, BaseModel):
    """
        used to model employee categories
    """
    name = models.CharField(max_length=35, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='%(app_label)s_%(class)s_sub_employee_categories')

    class MPTTMeta:
        order_insertion_by = ['name']
        ordering = ['name']
        app_label = 'core'

    def __str__(self):
        return '{name}'.format(name=self.name)


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

    class Meta:
        app_label = 'core'
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)

    @classmethod
    def get_user_or_none(cls, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    @classmethod
    def get_user_facility_or_none(cls, user):
        """
            This class method returns the Facility this given user belongs to and None if there is no facility.
        """
        try:
            employee = Employee.objects.get(user__id=user.id)
            return employee.current_company.facility
        except (Employee.DoesNotExist, Exception, ):
            return None


class ProcessingPeriod(BaseModel):
    """
        Used to model start and end date of processing or carrying out an action.
    """
    name = models.CharField(max_length=35, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        app_label = 'core'

    def __str__(self):
        return '{name}'.format(name=self.name)


class ProductCategory(MPTTModel, BaseModel):
    """
       This is used group products, it is hierarchical. it can be device, vaccine, diluent, syringes etc
    """
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='sub_product_categories')

    class MPTTMeta:
        order_insertion_by = ['name']
        ordering = ['name']
        app_label = 'core'

    def __str__(self):
        return '{name}'.format(name=self.name)


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

    class Meta:
        ordering = ['code']
        app_label = 'core'

    def __str__(self):
        return '{name}'.format(name=self.name)


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

    class Meta:
        app_label = 'core'
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)


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

    class Meta:
        app_label = 'core'
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)


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
    batch_no = models.CharField(max_length=35)
    bar_code = models.CharField(max_length=255, blank=True)
    gtin = models.CharField(max_length=35, blank=True)
    price_per_unit = models.DecimalField(max_digits=21, decimal_places=2)
    price_currency = models.ForeignKey(Currency, blank=True, null=True)
    expiration_date = models.DateField()
    mode_of_use = models.ForeignKey('ModeOfAdministration', blank=True, null=True)
    formulation = models.ForeignKey('ProductFormulation', blank=True, null=True)
    description = models.CharField(max_length=100, blank=True)
    weight_per_unit = models.FloatField(max_length=21, blank=True, null=True)
    weight_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True, related_name='product_item_weight_uom')
    volume_per_unit = models.FloatField(blank=True, null=True)
    volume_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True, related_name='product_item_volume_uom')
    active = models.BooleanField()

    class Meta:
        app_label = 'core'
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)


class ProductFormulation(BaseModel):
    """
        This model is for specifying product form, for vaccines and Diluent it can be Liquid, Lyophilised and
        Not Available for devices it is not applicable to.
    """
    name = models.CharField(max_length=55, unique=True)
    description = models.CharField(max_length=100, blank=True)


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
reversion.register(ProcessingPeriod)
reversion.register(ProductCategory)
reversion.register(Product)
reversion.register(ProductPresentation)
reversion.register(ModeOfAdministration)
reversion.register(ProductItem)
reversion.register(ProductFormulation)

