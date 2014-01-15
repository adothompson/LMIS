"""
    Inventory/models.py is the module that holds all the domain models etc that are used mainly for
    Inventory management
"""

#import core django modules
from django.db import models
from django.utils.translation import ugettext as _

#import external modules
import reversion
from model_utils import Choices

#import project modules
from cce.models import ColdChainEquipment
from core.models import BaseModel, ProductItem, UnitOfMeasurement, Employee, VVMStage, Program
from orders.models import Voucher
from facilities.models import Warehouse, Facility


class Inventory(BaseModel):
    """
        This is used to track the current quantity of each product at a warehouse. each facility warehouse
        (storage location) has an inventory.

        the cce link will enable us to keep track of inventory at CCE level.

    """
    warehouse = models.ForeignKey(Warehouse)
    cce = models.ForeignKey(ColdChainEquipment, blank=True, null=True)


class InventoryLine(BaseModel):
    """
        This represents a single entry for a unique stocks in an inventory

        The quantity unit of measurement is calculated from ProductItem->product->base_uom, likewise product code

        active - is used to indicate if the inventory line should be considered when calculating current quantity of
        a product at a facility etc.
    """
    product_item = models.ForeignKey(ProductItem)
    program = models.ForeignKey(Program)
    inventory = models.ForeignKey(Inventory, related_name='inventory_lines')
    quantity = models.IntegerField()
    weight = models.FloatField(blank=True, null=True)
    weight_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True,
                                   related_name='%(app_label)s_%(class)s_weight_uom')
    volume = models.FloatField(blank=True, null=True)
    volume_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True,
                                   related_name='%(app_label)s_%(class)s_volume_uom')
    active = models.BooleanField()


class InventoryLineAdjustment(BaseModel):
    """
        A one-to-many model for linking an inventory line to adjustments
    """
    inventory_line = models.ForeignKey(InventoryLine)
    adjustment = models.OneToOneField('Adjustment')


class FacilityActivity(BaseModel):
    """
        This is abstract base model for activities that are performed at Facilities such as PhysicalStockCount,
        recording ConsumptionRecord
    """
    facility = models.ForeignKey(Facility)
    performed_by = models.ForeignKey(Employee)
    verified_by = models.ForeignKey(Employee, related_name='%(app_label)s_%(class)s_verifier')

    class Meta:
        abstract = True


class PhysicalStockCount(FacilityActivity):
    """
        This is used record physical stock counts results.
    """
    pass


class PhysicalStockCountLine(BaseModel):
    """
        This is used to record each unique product item counted during physical stock count
    """
    product_item = models.ForeignKey(ProductItem)
    program = models.ForeignKey(Program)
    physical_stock_count = models.ForeignKey(PhysicalStockCount)
    physical_quantity = models.IntegerField(verbose_name='%(app_label)s_%(class)s_counted_quantity')
    inventory_quantity = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement, related_name='%(app_label)s_%(class)s_quantity_uom')
    vvm_stage = models.IntegerField(choices=VVMStage.STAGES, blank=True, null=True)
    comment = models.CharField(max_length=35, blank=True)


class PhysicalStockCountLineAdjustment(BaseModel):
    """
        This is used to model the one-to-many relationship between Physical Stock Count Line and Adjustments
    """
    physical_stock_line = models.ForeignKey(PhysicalStockCountLine)
    adjustment = models.OneToOneField('Adjustment')


class ConsumptionRecord(FacilityActivity):
    """
        This is used to keep track of product consumptions at a facility within a given period.
    """
    start_date = models.DateField()
    end_date = models.DateField()


class ConsumptionRecordLine(BaseModel):
    """
        ConsumptionRecordLine represents the quantity of each product item consumed at a facility within the
        ConsumptionRecord start and end date

        previous_balance = stock balance before start date
    """
    product_item = models.ForeignKey(ProductItem)
    program = models.ForeignKey(Program)
    previous_balance = models.IntegerField()
    quantity_used = models.IntegerField()
    current_balance = models.IntegerField()
    quantity_received = models.IntegerField()
    consumption_record = models.ForeignKey(ConsumptionRecord)
    total_discarded = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement)


class ConsumptionRecordLineAdjustment(BaseModel):
    """
        This is used to link ConsumptionRecordLine to adjustments
    """
    consumption_record_line = models.ForeignKey(ConsumptionRecordLine)
    adjustment = models.OneToOneField('Adjustment')


class StockEntry(BaseModel):
    """
        This is used to indicate different types of stock entry.

            Previous Balance: balance from previous year.

            New Arrival: stock entry type used to record quantity received from supplier

            Surplus: stock entry type used to record excess quantity recorded from physical stock count.

            Return: stock entry type used to record stock received from lower level stores.

            Other Sources: stock entry type used to record stock received from other sources

    """
    TYPES = Choices((0, 'previous_balance', ('Previous Balance')), (1, 'new_arrival', ('New Arrival')),
                    (2, 'surplus', ('Surplus')), (3, 'return', ('Return')), (4, 'others', ('Other Sources')))

    class Meta:
            managed = False


class IncomingShipment(BaseModel):
    """
        This is used to record stock arrival from supplier or supplying facility.

        input_warehouse - is the storage location of the recipient, where the product item will be kept.
        from the input_warehouse.facility we can get the facility that received the shipment.

        This can also be used to record excess quantity recorded during physical stock count by recording the exact
        product-item and the excess quantity
    """
    supplier = models.ForeignKey(Facility)
    stock_entry_type = models.IntegerField(choices=StockEntry.TYPES)
    input_warehouse = models.ForeignKey(Warehouse)
    other = models.BooleanField(default=False)
    other_source = models.CharField(max_length=35, blank=True, help_text='Enter source of shipment if stock entry type '
                                                                        'is "Other".')


class IncomingShipmentLine(BaseModel):
    """
        This is used to record the detail of each unique item of an IncomingShipment
    """
    incoming_shipment = models.ForeignKey(IncomingShipment, related_name='incoming_shipment_lines')
    product_item = models.ForeignKey(ProductItem)
    quantity = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement,
                                     related_name='%(app_label)s_%(class)s_quantity_uom')
    weight = models.FloatField(blank=True, null=True)
    weight_uom = models.ForeignKey(UnitOfMeasurement, related_name='%(app_label)s_%(class)s_weight_uom')
    packed_volume = models.FloatField(blank=True, null=True)
    packed_volume_uom = models.ForeignKey(UnitOfMeasurement, related_name='%(app_label)s_%(class)s_packed_volume_uom')
    vvm_stage = models.IntegerField(choices=VVMStage.STAGES, blank=True, null=True)
    voucher = models.ForeignKey(Voucher, blank=True, null=True)


class OutgoingShipment(BaseModel):
    """
        This is used to track stock movements out to recipient or receiving facility

        output_warehouse is the storage location the product item will be shipped from and it belongs to the supplying
        facility from the output_warehouse: we can get the facility that made the supply.
    """
    STATUS = Choices((0, 'draft', ('Draft')), (1, 'assigned', ('Assigned')), (2, 'done', ('Done')),
                     (3, 'cancelled', ('Cancelled'))
                     )
    recipient = models.ForeignKey(Facility)
    output_warehouse = models.ForeignKey(Warehouse)
    status = models.IntegerField(choices=STATUS)


class OutgoingShipmentLine(BaseModel):
    """
        This is used to record the detail of each unique product item of an OutgoingShipment
    """
    outgoing_shipment = models.ForeignKey(OutgoingShipment, related_name='outgoing_shipment_lines')
    product_item = models.ForeignKey(ProductItem)
    quantity_issued = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement, related_name='%(app_label)s_%(class)s_quantity_uom')
    weight_issued = models.FloatField(blank=True, null=True)
    weight_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True,
                                   related_name='%(app_label)s_%(class)s_weight_uom')
    volume = models.FloatField(blank=True, null=True)
    volume_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True,
                                   related_name='%(app_label)s_%(class)s_volume_uom')
    quantity_before = models.IntegerField()
    quantity_after = models.IntegerField()
    remark = models.CharField(max_length=55, blank=True, null=True)


class AdjustmentType(BaseModel):
    """
        Adjustment Types:
            Broken: this is adjustment type for quantity discarded due to breakage.
            Expired: this is adjustment type for quantity discarded due to expiration.
            Frozen: this is adjustment type for quantity discarded due to freezing.
            VVM: this is adjustment type for quantity discarded due to VVM change.
            Missing: this is adjustment type for missing quantity recorded during physical stock count.
            Others: this is adjustment type for quantity distributed to others.
    """
    TYPES = Choices((0, 'broken', ('Broken')), (1, 'expired', ('Expired')), (2, 'frozen', ('Frozen')),
                    (3, 'vvm', ('VVM')), (4, 'missing', ('Missing')), (5, 'others', ('Others')))

    class Meta:
        managed = False


class Adjustment(BaseModel):
    """
        Adjustment is used to account for difference between physical stock count quantities and inventory quantity.
        It is used to reconcile the difference between Physical stock count quantity and inventory quantity for an
        item.
    """
    previous_quantity = models.IntegerField()
    revised_quantity = models.IntegerField()
    adjustment_type = models.IntegerField(choices=AdjustmentType.TYPES)
    reason = models.CharField(max_length=55, verbose_name='reason for adjustment')


#register models that will be tracked by Reversion
reversion.register(Inventory)
reversion.register(InventoryLine)
reversion.register(PhysicalStockCount)
reversion.register(PhysicalStockCountLine)
reversion.register(ConsumptionRecord)
reversion.register(ConsumptionRecordLine)
reversion.register(IncomingShipment)
reversion.register(IncomingShipmentLine)
reversion.register(OutgoingShipment)
reversion.register(OutgoingShipmentLine)
reversion.register(Adjustment)