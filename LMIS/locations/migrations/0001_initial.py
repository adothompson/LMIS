# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocationType'
        db.create_table('locations_locationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sub_name', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('code', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=10)),
        ))
        db.send_create_signal('locations', ['LocationType'])

        # Adding model 'Location'
        db.create_table('locations_location', (
            ('parent', self.gf('mptt.fields.TreeForeignKey')(to=orm['locations.Location'], null=True, related_name='children')),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, default='Unknown')),
            ('alt_names', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('location_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.LocationType'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('locations', ['Location'])

        # Adding model 'GeoPoly'
        db.create_table('locations_geopoly', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('location', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['locations.Location'], null=True, related_name='poly', unique=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=36)),
            ('global_id_text', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('code', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('parent_code', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('source', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('last_modified_gis', self.gf('django.db.models.fields.DateField')(null=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('locations', ['GeoPoly'])

        # Adding model 'GeoPoint'
        db.create_table('locations_geopoint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('location', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['locations.Location'], null=True, related_name='point', unique=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=36)),
            ('global_id_text', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('code', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('parent_code', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('source', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime.now)),
            ('last_modified_gis', self.gf('django.db.models.fields.DateField')(null=True)),
            ('category', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal('locations', ['GeoPoint'])


    def backwards(self, orm):
        # Deleting model 'LocationType'
        db.delete_table('locations_locationtype')

        # Deleting model 'Location'
        db.delete_table('locations_location')

        # Deleting model 'GeoPoly'
        db.delete_table('locations_geopoly')

        # Deleting model 'GeoPoint'
        db.delete_table('locations_geopoint')


    models = {
        'locations.geopoint': {
            'Meta': {'object_name': 'GeoPoint'},
            'category': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'code': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'global_id_text': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'last_modified_gis': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['locations.Location']", 'null': 'True', 'related_name': "'point'", 'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'parent_code': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'source': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'uuid': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '36'})
        },
        'locations.geopoly': {
            'Meta': {'object_name': 'GeoPoly'},
            'code': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'global_id_text': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'last_modified_gis': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['locations.Location']", 'null': 'True', 'related_name': "'poly'", 'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'parent_code': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'source': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'uuid': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '36'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'alt_names': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.LocationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'Unknown'"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['locations.Location']", 'null': 'True', 'related_name': "'children'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'locations.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'code': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['locations']