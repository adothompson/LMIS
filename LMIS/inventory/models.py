#import core django modules
from django.db import models

#import project modules
from core.models import Warehouse, BaseModel, Item, UnitOfMeasurement


class Inventory(BaseModel):
    """
        This is used to track the current quantity of each product at a facility. each facility warehouse
        (storage location) has an inventory.
    """
    warehouse = models.ForeignKey(Warehouse, blank=True, null=True)


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
    weight_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    volume_uom = models.ForeignKey(UnitOfMeasurement, blank=True, null=True)
    active = models.BooleanField()





