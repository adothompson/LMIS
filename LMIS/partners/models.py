from django.db import models


from core.models import BaseModel, Company, Currency, Product


class Program(BaseModel):
    """
        Program is used to represent different types of health programs that facilities runs. ARV, HIV, KIck Polio
    """
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=55, blank=True)
    active = models.BooleanField()
    partners = models.ManyToManyField(Company)

    class Meta:
        app_label = 'partners'

    def __str__(self):
        return '{name}'.format(name=self.name)


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
        app_label = 'partners'


class ProgramProduct(BaseModel):
    """
        ProgramProduct models set of products that can be used in a Program.
        it is recorded for each product used in a program

        -unit_per_target is the number of base units of the product required per person(in the target population)
         to complete treatment or immunization.
    """
    program = models.ForeignKey(Program)
    product = models.ForeignKey(Product)
    allocation_info = models.OneToOneField(ProgramProductAllocationInfo)
    unit_per_target = models.IntegerField()
    current_price_per_unit = models.DecimalField(max_digits=21, decimal_places=2, verbose_name='price per uom')
    price_currency = models.ForeignKey(Currency, blank=True, null=True)
    funding_source = models.ManyToManyField(Company)
    is_active = models.BooleanField()

    class Meta:
        app_label = 'partners'

    def __str__(self):
        return '{program}-{product}'.format(program=self.program.name, product=self.product.name)