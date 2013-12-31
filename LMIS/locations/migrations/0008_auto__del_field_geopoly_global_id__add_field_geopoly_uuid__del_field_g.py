# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'GeoPoly.global_id'
        db.delete_column('locations_geopoly', 'global_id')

        # Adding field 'GeoPoly.uuid'
        db.add_column('locations_geopoly', 'uuid',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=36, null=True),
                      keep_default=False)

        # Deleting field 'GeoPoint.global_id'
        db.delete_column('locations_geopoint', 'global_id')

        # Adding field 'GeoPoint.uuid'
        db.add_column('locations_geopoint', 'uuid',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=36, null=True),
                      keep_default=False)

        # Deleting field 'Location.global_id'
        db.delete_column('locations_location', 'global_id')

        # Deleting field 'Location.id'
        db.delete_column('locations_location', 'id')

        # Adding field 'Location.uuid'
        db.add_column('locations_location', 'uuid',
                      self.gf('django.db.models.fields.CharField')(default='', primary_key=True, max_length=36),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'GeoPoly.global_id'
        db.add_column('locations_geopoly', 'global_id',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=36, null=True),
                      keep_default=False)

        # Deleting field 'GeoPoly.uuid'
        db.delete_column('locations_geopoly', 'uuid')

        # Adding field 'GeoPoint.global_id'
        db.add_column('locations_geopoint', 'global_id',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=36, null=True),
                      keep_default=False)

        # Deleting field 'GeoPoint.uuid'
        db.delete_column('locations_geopoint', 'uuid')

        # Adding field 'Location.global_id'
        db.add_column('locations_location', 'global_id',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=36, null=True, unique=True),
                      keep_default=False)

        # Adding field 'Location.id'
        db.add_column('locations_location', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Deleting field 'Location.uuid'
        db.delete_column('locations_location', 'uuid')


    models = {
        'locations.geopoint': {
            'Meta': {'object_name': 'GeoPoint'},
            'category': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'global_id_text': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'last_modified_gis': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['locations.Location']", 'unique': 'True', 'related_name': "'point'", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'parent_code': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '36', 'null': 'True'})
        },
        'locations.geopoly': {
            'Meta': {'object_name': 'GeoPoly'},
            'code': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'global_id_text': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'last_modified_gis': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['locations.Location']", 'unique': 'True', 'related_name': "'poly'", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'parent_code': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '36', 'null': 'True'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'alt_names': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.LocationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['locations.Location']", 'related_name': "'children'", 'null': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'locations.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'code': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['locations']