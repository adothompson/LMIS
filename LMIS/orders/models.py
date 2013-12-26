#import core django module.
from django.db import models

#import project modules
from core.models import BaseModel, Facility, Product, UnitOfMeasurement


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
    facility = models.ForeignKey(Facility)
    status = models.IntegerField(choices=STATUS)
    order_date = models.DateField()
    expected_date = models.DateField(blank=True, null=True)
    emergency = models.BooleanField(default=False)


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
