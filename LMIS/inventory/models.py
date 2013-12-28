#import core django modules
from django.db import models

#import project modules
from cce.models import ColdChainEquipment
from core.models import Warehouse, BaseModel, Item, UnitOfMeasurement, Facility, Employee, VVMStage, Company
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

        The quantity unit of measurement is calculated from Item->product->base_uom, likewise product code

        active - is used to indicate if the inventory line should be considered when calculating current quantity of
        a product at a facility etc.
    """
    item = models.ForeignKey(Item)
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
    date = models.DateField()
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
        This is used to record each unique item counted during physical stock count
    """
    item = models.ForeignKey(Item)
    physical_stock_count = models.ForeignKey(PhysicalStockCount)
    quantity = models.IntegerField(verbose_name='physically counted quantity')
    inventory_quantity = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement)
    vvm_stage = models.IntegerField(choices=VVMStage.STAGE, blank=True, null=True)
    comment = models.CharField(blank=True)


class ConsumptionRecord(FacilityActivity):
    """
        This is used to keep track of product consumptions at a facility within a given period.
    """
    start_date = models.DateField()
    end_date = models.DateField()


class ConsumptionRecordLine(BaseModel):
    """
        ConsumptionRecordLine represents the quantity of each item consumed at a facility within the ConsumptionRecord
        start and end date
    """
    item = models.ForeignKey(Item)
    consumption_record = models.ForeignKey(ConsumptionRecord)
    quantity_dispensed = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement)


class IncomingShipment(BaseModel):
    """
        This is used to record stock arrival from supplier or supplying facility.

        warehouse - is the storage location of the recipient, where the item will be kept.
    """
    supplier = models.ForeignKey(Facility)
    input_warehouse = models.ForeignKey(Warehouse)
    created_date = models.DateField()
    others = models.BooleanField(default=False)
    other_source = models.CharField()


class IncomingShipmentLine(BaseModel):
    """
        This is used to record the detail of each unique item of an IncomingShipment
    """
    item = models.ForeignKey(Item)
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

        output_warehouse is the storage location the item will be shipped from.
    """
    uuid = UUIDField(version=4, primary_key=True)
    STATUS = (
        (0, 'Draft'),
        (1, 'Received'),
        (2, 'Cancelled')
    )
    recipient = models.ForeignKey(Facility)
    output_warehouse = models.ForeignKey(Warehouse)
    created_date = models.DateField()
    status = models.IntegerField(choices=STATUS)


class OutgoingShipmentLine(BaseModel):
    """
        This is used to record the detail of each unique item of an OutgoingShipment
    """
    uuid = UUIDField(version=4, primary_key=True)
    item = models.ForeignKey(Item)
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