# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocationType'
        db.create_table(u'locations_locationtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'locations', ['LocationType'])

        # Adding model 'Location'
        db.create_table(u'locations_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(related_name=u'children', null=True, to=orm['locations.Location'])),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'Unknown', max_length=100)),
            ('alt_names', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('location_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.LocationType'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'locations', ['Location'])

        # Adding model 'GeoPoly'
        db.create_table(u'locations_geopoly', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'poly', unique=True, null=True, to=orm['locations.Location'])),
            ('global_id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'locations', ['GeoPoly'])

        # Adding model 'GeoPoint'
        db.create_table(u'locations_geopoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'point', unique=True, null=True, to=orm['locations.Location'])),
            ('global_id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'locations', ['GeoPoint'])


    def backwards(self, orm):
        # Deleting model 'LocationType'
        db.delete_table(u'locations_locationtype')

        # Deleting model 'Location'
        db.delete_table(u'locations_location')

        # Deleting model 'GeoPoly'
        db.delete_table(u'locations_geopoly')

        # Deleting model 'GeoPoint'
        db.delete_table(u'locations_geopoint')


    models = {
        u'locations.geopoint': {
            'Meta': {'object_name': 'GeoPoint'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'global_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'point'", 'unique': 'True', 'null': 'True', 'to': u"orm['locations.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'locations.geopoly': {
            'Meta': {'object_name': 'GeoPoly'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'global_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'poly'", 'unique': 'True', 'null': 'True', 'to': u"orm['locations.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'locations.location': {
            'Meta': {'object_name': 'Location'},
            'alt_names': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.LocationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u'Unknown'", 'max_length': '100'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "u'children'", 'null': 'True', 'to': u"orm['locations.Location']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'locations.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['locations']