# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ColdChainEquipmentType'
        db.create_table('cce_coldchainequipmenttype', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, related_name='cce_coldchainequipmenttype_created_by', blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, related_name='cce_coldchainequipmenttype_modified_by', blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True)),
            ('minimum_temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('maximum_temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('temperature_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.UnitOfMeasurement'])),
        ))
        db.send_create_signal('cce', ['ColdChainEquipmentType'])

        # Adding model 'ColdChainEquipment'
        db.create_table('cce_coldchainequipment', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, related_name='cce_coldchainequipment_created_by', blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, related_name='cce_coldchainequipment_modified_by', blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('gross_capacity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('net_capacity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('capacity_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.UnitOfMeasurement'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cce.ColdChainEquipmentType'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('storage_location', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['facilities.Warehouse'])),
        ))
        db.send_create_signal('cce', ['ColdChainEquipment'])

        # Adding model 'CCETemperatureLog'
        db.create_table('cce_ccetemperaturelog', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, related_name='cce_ccetemperaturelog_created_by', blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, related_name='cce_ccetemperaturelog_modified_by', blank=True)),
            ('temperature', self.gf('django.db.models.fields.FloatField')()),
            ('temperature_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'])),
            ('cce', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cce.ColdChainEquipment'])),
            ('date_time_logged', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('cce', ['CCETemperatureLog'])

        # Adding model 'CCEProblemLog'
        db.create_table('cce_cceproblemlog', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, related_name='cce_cceproblemlog_created_by', blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, related_name='cce_cceproblemlog_modified_by', blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('cce', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cce.ColdChainEquipment'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('cce', ['CCEProblemLog'])


    def backwards(self, orm):
        # Deleting model 'ColdChainEquipmentType'
        db.delete_table('cce_coldchainequipmenttype')

        # Deleting model 'ColdChainEquipment'
        db.delete_table('cce_coldchainequipment')

        # Deleting model 'CCETemperatureLog'
        db.delete_table('cce_ccetemperaturelog')

        # Deleting model 'CCEProblemLog'
        db.delete_table('cce_cceproblemlog')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'cce.cceproblemlog': {
            'Meta': {'object_name': 'CCEProblemLog'},
            'cce': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cce.ColdChainEquipment']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'cce_cceproblemlog_created_by'", 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'cce_cceproblemlog_modified_by'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'cce.ccetemperaturelog': {
            'Meta': {'object_name': 'CCETemperatureLog'},
            'cce': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cce.ColdChainEquipment']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'cce_ccetemperaturelog_created_by'", 'blank': 'True'}),
            'date_time_logged': ('django.db.models.fields.DateTimeField', [], {}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'cce_ccetemperaturelog_modified_by'", 'blank': 'True'}),
            'temperature': ('django.db.models.fields.FloatField', [], {}),
            'temperature_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'cce.coldchainequipment': {
            'Meta': {'object_name': 'ColdChainEquipment'},
            'capacity_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.UnitOfMeasurement']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'cce_coldchainequipment_created_by'", 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'cce_coldchainequipment_modified_by'", 'blank': 'True'}),
            'net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'storage_location': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['facilities.Warehouse']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cce.ColdChainEquipmentType']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'cce.coldchainequipmenttype': {
            'Meta': {'object_name': 'ColdChainEquipmentType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'cce_coldchainequipmenttype_created_by'", 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'maximum_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'cce_coldchainequipmenttype_modified_by'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'temperature_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.address': {
            'Meta': {'ordering': "['tag']", 'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_address_created_by'", 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_address_modified_by'", 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'subdivision': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'core.company': {
            'Meta': {'ordering': "['name']", 'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Address']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.CompanyCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Contact']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_company_created_by'", 'blank': 'True'}),
            'footer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_company_modified_by'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'null': 'True', 'to': "orm['core.Product']", 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_companycategory_created_by'", 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_companycategory_modified_by'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['core.CompanyCategory']", 'null': 'True', 'related_name': "'core_companycategory_sub_company_categories'", 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.contact': {
            'Meta': {'ordering': "['tag']", 'object_name': 'Contact'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_contact_created_by'", 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'irc': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_contact_modified_by'", 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'sip': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'core.product': {
            'Meta': {'ordering': "['code']", 'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'base_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_product_created_by'", 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_product_modified_by'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_productcategory_created_by'", 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_productcategory_modified_by'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['core.ProductCategory']", 'null': 'True', 'related_name': "'sub_product_categories'", 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.unitofmeasurement': {
            'Meta': {'ordering': "['name']", 'object_name': 'UnitOfMeasurement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_unitofmeasurement_created_by'", 'blank': 'True'}),
            'factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_unitofmeasurement_modified_by'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rounding_precision': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uom_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UOMCategory']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.uomcategory': {
            'Meta': {'object_name': 'UOMCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_uomcategory_created_by'", 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'core_uomcategory_modified_by'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['core.UOMCategory']", 'null': 'True', 'related_name': "'core_uomcategory_sub_uom_categories'", 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'facilities.facility': {
            'Meta': {'object_name': 'Facility', '_ormbases': ['core.Company']},
            'catchment_population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['core.Company']", 'unique': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'facility_operators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'facility_operators'", 'null': 'True', 'to': "orm['core.Company']", 'blank': 'True'}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.FacilityType']"}),
            'global_location_no': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'go_down_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'go_live_date': ('django.db.models.fields.DateField', [], {}),
            'has_electricity': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_electronic_dar': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_electronic_scc': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True', 'default': 'True'}),
            'is_online': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_satellite': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['locations.Location']"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['facilities.Facility']", 'null': 'True', 'related_name': "'child_facilities'", 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'sdp': ('django.db.models.fields.BooleanField', [], {}),
            'supplies_others': ('django.db.models.fields.BooleanField', [], {}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'virtual_facility': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'facilities.facilitytype': {
            'Meta': {'object_name': 'FacilityType'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'facilities_facilitytype_created_by'", 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'facilities_facilitytype_modified_by'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['facilities.FacilityType']", 'null': 'True', 'related_name': "'sub_facility_types'", 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'facilities.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'ambient_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ambient_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'cold_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cold_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'facilities_warehouse_created_by'", 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_refrigerated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'facilities_warehouse_modified_by'", 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'alt_names': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.LocationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'Unknown'"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'related_name': "'children'", 'to': "orm['locations.Location']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'locations.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cce']