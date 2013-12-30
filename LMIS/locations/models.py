#!/usr/bin/env python
# encoding=utf-8
from __future__ import unicode_literals
from datetime import date
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.gis.db import models as geomodels
from django_extensions.db import fields as ext_fields


class LocationType(models.Model):
    name = models.CharField(max_length=100)
    sub_name = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        if self.sub_name is None:
            return u"%s" % self.name
        else:
            return u"%s-%s" % (self.name, self.sub_name)

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = "Location Type"


class Location(MPTTModel):
    parent = TreeForeignKey('self', null=True, related_name='children')
    global_id = ext_fields.UUIDField(version=4, unique=True, null=True)
    name = models.CharField(max_length=100, default="Unknown")
    alt_names = models.CharField(max_length=200, null=True, blank=True)
    location_type = models.ForeignKey(LocationType)
    created_at = ext_fields.CreationDateTimeField()
    last_modified = ext_fields.ModificationDateTimeField()

    @property
    def gis(self):
        try:
            return self.poly
        except GeoPoly.DoesNotExist:
            try:
                return self.point
            except GeoPoint.DoesNotExist:
                return None

    def __str__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name = "Location"


class GeoPoly(geomodels.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.OneToOneField(Location, null=True, related_name='poly')
    global_id = ext_fields.UUIDField(version=4, null=True)
    global_id_text = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    parent_code = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    created_at = ext_fields.CreationDateTimeField()
    last_modified = ext_fields.ModificationDateTimeField()
    last_modified_gis = models.DateField(null=True)

    geom = geomodels.MultiPolygonField(srid=4326)
    objects = geomodels.GeoManager()

    class Meta:
        verbose_name = "Geo Location Polygon"


class GeoPoint(geomodels.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.OneToOneField(Location, null=True, related_name='point')
    global_id = ext_fields.UUIDField(version=4, null=True)
    global_id_text = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    parent_code = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    created_at = ext_fields.CreationDateTimeField()
    last_modified = ext_fields.ModificationDateTimeField()
    last_modified_gis = models.DateField(null=True)
    category = models.CharField(max_length=100, null=True, blank=True)

    geom = geomodels.PointField(srid=4326)
    objects = geomodels.GeoManager()

    class Meta:
        verbose_name = "Geo Location Point"
