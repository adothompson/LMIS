#import django modules
from django.db import models
from django.core.exceptions import ValidationError

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
    uom_category = models.ForeignKey(UOMCategory)
    rate = models.FloatField(null=True, blank=True)
    factor = models.FloatField(null=True, blank=True)
    rounding_precision = models.IntegerField(max_length=2, blank=True, null=True)

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        app_label = 'core'


class Rate(BaseModel):
    """ This belongs to the currency class and is used to model different exchange rates for the currency.
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
    name = models.CharField(max_length=35, unique=True)
    code = models.CharField(max_length=25, unique=True)
    contact = models.ForeignKey(Contact, null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True)

    class Meta:
        abstract = True

    class Meta:
        app_label = 'core'