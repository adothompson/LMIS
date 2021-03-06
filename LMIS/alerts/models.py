"""
    This module handles sending of sms, emails and setting on-site notification.
"""

#import core django modules
from django.db import models

#import external modules
import reversion
from model_utils import Choices

#import project modules
from core.models import BaseModel, Facility, Employee


class Priority(BaseModel):
    """
        This is used to model notification priority levels
    """
    LEVELS = Choices((0, 'low', ('Low')), (1, 'medium', ('Medium')), (2, 'high', ('High')),
                     (3, 'critical', ('Critical')))

    class Meta:
        managed = False


class OnSiteNotification(BaseModel):
    """
        This is used to log each on-site notification flag.
    """
    source = models.ForeignKey(Facility, related_name='source')
    destination = models.ForeignKey(Facility, related_name='destination')
    message = models.CharField(max_length=200)
    priority_level = models.IntegerField(choices=Priority.LEVELS)
    date_time = models.DateTimeField()


class OnSiteNotificationRecipient(BaseModel):
    """
        This is used to keep track of notification recipients and whether they have seen the notification or not.
    """
    recipient = models.ForeignKey(Employee)
    seen = models.BooleanField(default=False)
    resolved = models.BooleanField(default=False)


#register models that will be tracked with reversion

reversion.register(OnSiteNotification)
reversion.register(OnSiteNotificationRecipient)

