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
            ('sub_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True, null=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True, null=True)),
        ))
        db.send_create_signal('locations', ['LocationType'])

        # Adding model 'Location'
        db.create_table('locations_location', (
            ('parent', self.gf('mptt.fields.TreeForeignKey')(related_name='children', null=True, to=orm['locations.Location'])),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=100)),
            ('alt_names', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True, null=True)),
            ('location_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.LocationType'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('locations', ['Location'])

        # Adding model 'GeoPoly'
        db.create_table('locations_geopoly', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True, null=True)),
            ('location', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, related_name='poly', null=True, to=orm['locations.Location'])),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True, null=True)),
            ('global_id_text', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True, null=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True, null=True)),
            ('parent_code', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True, null=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('last_modified_gis', self.gf('django.db.models.fields.DateField')(null=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('locations', ['GeoPoly'])

        # Adding model 'GeoPoint'
        db.create_table('locations_geopoint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True, null=True)),
            ('location', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, related_name='point', null=True, to=orm['locations.Location'])),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True, null=True)),
            ('global_id_text', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True, null=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True, null=True)),
            ('parent_code', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True, null=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('last_modified_gis', self.gf('django.db.models.fields.DateField')(null=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True, null=True)),
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
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'global_id_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'last_modified_gis': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'related_name': "'point'", 'null': 'True', 'to': "orm['locations.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'parent_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True', 'null': 'True'})
        },
        'locations.geopoly': {
            'Meta': {'object_name': 'GeoPoly'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'global_id_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'last_modified_gis': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'related_name': "'poly'", 'null': 'True', 'to': "orm['locations.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'parent_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True', 'null': 'True'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'alt_names': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.LocationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'children'", 'null': 'True', 'to': "orm['locations.Location']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'locations.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['locations']