#!/usr/bin/env python
# encoding=utf-8

from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from .models import LocationType, Location, GeoPoint, GeoPoly


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_type', 'uuid')
    list_filter = ('location_type', )
    search_fields = ('name', )


class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_name')


class GeoPolyAdmin(geoadmin.OSMGeoAdmin):
    list_display = ('name', 'location', 'uuid', 'code', 'parent_code', 'source',
                    'last_modified_gis')
    list_filter = ('location__location_type', 'source', )
    search_fields = ('name', 'code', 'source',)


class GeoPointAdmin(geoadmin.OSMGeoAdmin):
    list_display = ('name', 'location')
    list_filter = ('location__location_type', 'source', )
    search_fields = ('name', 'code', 'source',)


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationType, LocationTypeAdmin)
admin.site.register(GeoPoly, GeoPolyAdmin)
admin.site.register(GeoPoint, GeoPointAdmin)
