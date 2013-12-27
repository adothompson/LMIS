#import core django module.
from django.db import models

#import project modules
from core.models import BaseModel, Facility, Product, UnitOfMeasurement, Item, Currency, Employee


class PurchaseOrder(BaseModel):
    """
        PurchaseOrder: is used to request a Facility to supply product to the facility that placed the PurchaseOrder
        and it provides specifications and quantities.
    """
    STATUS = (
        (0, 'Draft'),
        (1, 'Assigned'),
        (2, 'Done'),
        (3, 'Cancelled')
    )
    purchaser = models.ForeignKey(Facility, related_name='purchaser')
    supplier = models.ForeignKey(Facility, related_name='supplier')
    status = models.IntegerField(choices=STATUS, default=0)
    emergency = models.BooleanField(default=False)
    order_date = models.DateField()
    expected_date = models.DateField(blank=True, null=True)
    sales_order = models.ForeignKey('SaleOrder', blank=True, null=True)


class PurchaseOrderLine(BaseModel):
    """
        PurchaseOrderLine defines product, quantity of product, current stock level of product at the requesting facility,
        it is used to fill an order.
    """
    models.ForeignKey(PurchaseOrder)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement)
    remark = models.CharField(max_length=55, blank=True)


class SalesOrder(BaseModel):
    """
        SalesOrder  is used by a Supplying Facility to record products, specifications and quantities that will be
        supplied to a receiving facility. it is usually linked to an PurchaseOrder.

        optionally, it can be linked to a purchase order.
    """
    recipient = models.ForeignKey(Facility, related_name='recipient')
    supplier = models.ForeignKey(Facility, related_name='supplier')
    approved_by = models.ForeignKey(Employee)
    #the date this was recorded in the system
    sales_date = models.DateField()
    planned_date = models.DateField(blank=True, null=True)
    completed_date = models.DateField(null=True, blank=True)


class SalesOrderLine(BaseModel):
    """
        This is used to model each product unique item that is part of a sales order.
    """
    sales_order = models.ForeignKey(SalesOrder)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement)
    price_per_base_uom = models.DecimalField(max_length=21, decimal_places=2)
    price_currency = models.FloatField(Currency)
    description = models.CharField(max_length=55, blank=True)


class Voucher(BaseModel):
    """

    """
    sales_order = models.ForeignKey(SalesOrder)