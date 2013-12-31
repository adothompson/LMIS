"""
    Inventory/models.py is the module that holds all the domain models etc that are used mainly for
    Inventory management
"""

#import core django modules
from django.db import models

#import external modules
from model_utils import Choices

#import project modules
from cce.models import ColdChainEquipment
from core.models import Warehouse, BaseModel, ProductItem, UnitOfMeasurement, Facility, Employee, VVMStage
from orders.models import Voucher


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
    inventory = models.ForeignKey(Inventory)
    quantity = models.IntegerField()
    weight = models.FloatField(blank=True, null=True)
    weight_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True, related_name='weight uom')
    volume = models.FloatField(blank=True, null=True)
    volume_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True, related_name='volume uom')
    active = models.BooleanField()


class FacilityActivity(BaseModel):
    """
        This is abstract base model for activities that are performed at Facilities such as PhysicalStockCount,
        recording ConsumptionRecord
    """
    facility = models.ForeignKey(Facility)
    performed_by = models.ForeignKey(Employee)
    verified_by = models.ForeignKey(Employee, related_name='verifier')

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
    physical_stock_count = models.ForeignKey(PhysicalStockCount)
    physical_quantity = models.IntegerField(verbose_name='physically counted quantity')
    inventory_quantity = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement)
    vvm_stage = models.IntegerField(choices=VVMStage.STAGES, blank=True, null=True)
    comment = models.CharField(blank=True)


class ConsumptionRecord(FacilityActivity):
    """
        This is used to keep track of product consumptions at a facility within a given period.
    """
    start_date = models.DateField()
    end_date = models.DateField()


class ConsumptionRecordLine(BaseModel):
    """
        ConsumptionRecordLine represents the quantity of each product item consumed at a facility within the ConsumptionRecord
        start and end date
    """
    product_item = models.ForeignKey(ProductItem)
    consumption_record = models.ForeignKey(ConsumptionRecord)
    quantity_dispensed = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement)


class StockEntry(BaseModel):
    """
        This is used to indicate different types of stock entry.

            New Arrival: stock entry type used to record quantity received from supplier

            Surplus: stock entry type used to record excess quantity recorded from physical stock count.

            Return: stock entry type used to record stock received from lower level stores.

            Other Sources: stock entry type used to record stock received from other sources

    """
    TYPES = Choices((0, 'new_arrival', _('New Arrival')), (1, 'surplus', _('Surplus')), (2, 'return', _('Return')),

                    (3, 'others', _('Other Sources')))

    class Meta:
            managed = False


class IncomingShipment(BaseModel):
    """
        This is used to record stock arrival from supplier or supplying facility.

        input_warehouse - is the storage location of the recipient, where the product item will be kept.
        from the input_warehouse.facility we can get the facility that received the shipment
    """
    supplier = models.ForeignKey(Facility)
    stock_entry_type = models.IntegerField(choices=StockEntry.TYPES)
    input_warehouse = models.ForeignKey(Warehouse)
    others = models.BooleanField(default=False)
    other_source = models.CharField()


class IncomingShipmentLine(BaseModel):
    """
        This is used to record the detail of each unique item of an IncomingShipment
    """
    product_item = models.ForeignKey(ProductItem)
    quantity_received = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement, related_name='quantity uom')
    stock_before = models.IntegerField()
    stock_after = models.IntegerField()
    stock_balance = models.IntegerField(blank=True, null=True)
    stock_balance_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True, related_name='stock balance uom')
    weight = models.FloatField(blank=True, null=True)
    weight_uom = models.ForeignKey(UnitOfMeasurement, related_name='weight uom')
    packed_volume = models.FloatField(blank=True, null=True)
    packed_volume_uom = models.ForeignKey(UnitOfMeasurement, related_name='packed volume uom')
    vvm_stage = models.ForeignKey(choices=VVMStage.STAGES, blank=True, null=True)
    voucher = models.ForeignKey(Voucher, blank=True, null=True)


class OutgoingShipment(BaseModel):
    """
        This is used to track stock movements out to recipient or receiving facility

        output_warehouse is the storage location the product item will be shipped from and it belongs to the supplying facility.
        from the output_warehouse: we can get the facility that made the supply.
    """
    STATUS = Choices((0, 'draft', _('Draft')), (1, 'assigned', _('Assigned')), (2, 'done', _('Done')),
                     (3, 'cancelled', _('Cancelled'))
                     )
    recipient = models.ForeignKey(Facility)
    stock_entry_type = models.IntegerField(choices=StockEntry.TYPES)
    output_warehouse = models.ForeignKey(Warehouse)
    status = models.IntegerField(choices=STATUS)


class OutgoingShipmentLine(BaseModel):
    """
        This is used to record the detail of each unique product item of an OutgoingShipment
    """
    product_item = models.ForeignKey(ProductItem)
    quantity_issued = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement, related_name='quantity uom')
    weight_issued = models.FloatField(blank=True, null=True)
    weight_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True, related_name='weight uom')
    volume = models.FloatField(blank=True, null=True)
    volume_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True, related_name='volume uom')
    stock_before = models.IntegerField()
    stock_after = models.IntegerField()
    stock_balance = models.IntegerField(blank=True, null=True)
    stock_balance_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True, related_name='stock balance uom')
    remark = models.CharField(blank=True, null=True)


class Adjustment(BaseModel):
    """
        Adjustment is used to account for difference between physical stock count quantities and inventory quantity.
        It is used to reconcile the difference between Physical stock count quantity and inventory quantity for an
        item.
        the physical stock count line is the physical stock count line the adjustment is for.
    """
    physical_stock_line = models.ForeignKey('PhysicalStockCountLine')
    previous_quantity = models.IntegerField()
    revised_quantity = models.IntegerField()
    reason = models.CharField(max_length=55, verbose_name='reason for adjustment')
    date_time = models.DateTimeField()