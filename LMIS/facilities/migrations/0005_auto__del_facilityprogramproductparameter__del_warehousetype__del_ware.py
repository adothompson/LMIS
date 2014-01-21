# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'FacilityProgramProductParameter'
        db.delete_table('facilities_facilityprogramproductparameter')

        # Deleting model 'WarehouseType'
        db.delete_table('facilities_warehousetype')

        # Deleting model 'Warehouse'
        db.delete_table('facilities_warehouse')

        # Deleting field 'FacilitySupportedProgramProduct.allocation_info'
        db.delete_column('facilities_facilitysupportedprogramproduct', 'allocation_info_id')

        # Adding field 'FacilitySupportedProgramProduct.who_ratio'
        db.add_column('facilities_facilitysupportedprogramproduct', 'who_ratio',
                      self.gf('django.db.models.fields.FloatField')(default=1),
                      keep_default=False)

        # Adding field 'FacilitySupportedProgramProduct.coverage_rate'
        db.add_column('facilities_facilitysupportedprogramproduct', 'coverage_rate',
                      self.gf('django.db.models.fields.FloatField')(default=1),
                      keep_default=False)

        # Adding field 'FacilitySupportedProgramProduct.wastage_rate'
        db.add_column('facilities_facilitysupportedprogramproduct', 'wastage_rate',
                      self.gf('django.db.models.fields.FloatField')(default=1),
                      keep_default=False)

        # Adding field 'FacilitySupportedProgramProduct.buffer_percentage'
        db.add_column('facilities_facilitysupportedprogramproduct', 'buffer_percentage',
                      self.gf('django.db.models.fields.FloatField')(default=1),
                      keep_default=False)

        # Adding field 'FacilitySupportedProgramProduct.target_population'
        db.add_column('facilities_facilitysupportedprogramproduct', 'target_population',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'FacilitySupportedProgramProduct.min_quantity'
        db.add_column('facilities_facilitysupportedprogramproduct', 'min_quantity',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'FacilitySupportedProgramProduct.max_quantity'
        db.add_column('facilities_facilitysupportedprogramproduct', 'max_quantity',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'FacilitySupportedProgramProduct.push'
        db.add_column('facilities_facilitysupportedprogramproduct', 'push',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'FacilitySupportedProgramProduct.lead_time'
        db.add_column('facilities_facilitysupportedprogramproduct', 'lead_time',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'FacilitySupportedProgramProduct.supply_interval'
        db.add_column('facilities_facilitysupportedprogramproduct', 'supply_interval',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'FacilityProgramProductParameter'
        db.create_table('facilities_facilityprogramproductparameter', (
            ('buffer_percentage', self.gf('django.db.models.fields.FloatField')()),
            ('max_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('supply_interval', self.gf('django.db.models.fields.IntegerField')()),
            ('who_ratio', self.gf('django.db.models.fields.FloatField')()),
            ('min_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('target_population', self.gf('django.db.models.fields.IntegerField')()),
            ('wastage_rate', self.gf('django.db.models.fields.FloatField')()),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, related_name='facilities_facilityprogramproductparameter_modified_by', null=True)),
            ('lead_time', self.gf('django.db.models.fields.IntegerField')()),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, related_name='facilities_facilityprogramproductparameter_created_by', null=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('push', self.gf('django.db.models.fields.BooleanField')()),
            ('coverage_rate', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('facilities', ['FacilityProgramProductParameter'])

        # Adding model 'WarehouseType'
        db.create_table('facilities_warehousetype', (
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, related_name='facilities_warehousetype_modified_by', null=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, related_name='facilities_warehousetype_created_by', null=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=35)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
        ))
        db.send_create_signal('facilities', ['WarehouseType'])

        # Adding model 'Warehouse'
        db.create_table('facilities_warehouse', (
            ('cold_storage_net_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('ambient_storage_gross_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('cold_storage_gross_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=55)),
            ('ambient_storage_net_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, related_name='facilities_warehouse_modified_by', null=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('is_refrigerated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, related_name='facilities_warehouse_created_by', null=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('facilities', ['Warehouse'])

        # Adding field 'FacilitySupportedProgramProduct.allocation_info'
        db.add_column('facilities_facilitysupportedprogramproduct', 'allocation_info',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['facilities.FacilityProgramProductParameter'], unique=True),
                      keep_default=False)

        # Deleting field 'FacilitySupportedProgramProduct.who_ratio'
        db.delete_column('facilities_facilitysupportedprogramproduct', 'who_ratio')

        # Deleting field 'FacilitySupportedProgramProduct.coverage_rate'
        db.delete_column('facilities_facilitysupportedprogramproduct', 'coverage_rate')

        # Deleting field 'FacilitySupportedProgramProduct.wastage_rate'
        db.delete_column('facilities_facilitysupportedprogramproduct', 'wastage_rate')

        # Deleting field 'FacilitySupportedProgramProduct.buffer_percentage'
        db.delete_column('facilities_facilitysupportedprogramproduct', 'buffer_percentage')

        # Deleting field 'FacilitySupportedProgramProduct.target_population'
        db.delete_column('facilities_facilitysupportedprogramproduct', 'target_population')

        # Deleting field 'FacilitySupportedProgramProduct.min_quantity'
        db.delete_column('facilities_facilitysupportedprogramproduct', 'min_quantity')

        # Deleting field 'FacilitySupportedProgramProduct.max_quantity'
        db.delete_column('facilities_facilitysupportedprogramproduct', 'max_quantity')

        # Deleting field 'FacilitySupportedProgramProduct.push'
        db.delete_column('facilities_facilitysupportedprogramproduct', 'push')

        # Deleting field 'FacilitySupportedProgramProduct.lead_time'
        db.delete_column('facilities_facilitysupportedprogramproduct', 'lead_time')

        # Deleting field 'FacilitySupportedProgramProduct.supply_interval'
        db.delete_column('facilities_facilitysupportedprogramproduct', 'supply_interval')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.address': {
            'Meta': {'ordering': "['tag']", 'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_address_created_by'"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_address_modified_by'"}),
            'street': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'subdivision': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10'}),
            'tag': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'zip': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'})
        },
        'core.company': {
            'Meta': {'ordering': "['name']", 'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['core.Address']", 'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.CompanyCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['core.Contact']", 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_company_created_by'"}),
            'footer': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_company_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Product']", 'symmetrical': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_companycategory_created_by'"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_companycategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.CompanyCategory']", 'related_name': "'core_companycategory_sub_company_categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.contact': {
            'Meta': {'ordering': "['tag']", 'object_name': 'Contact'},
            'comment': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_contact_created_by'"}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'irc': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jabber': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'mobile': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_contact_modified_by'"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'}),
            'sip': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '25'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'})
        },
        'core.currency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_currency_created_by'"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_currency_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '5', 'unique': 'True'}),
            'symbol_position': ('django.db.models.fields.CharField', [], {'default': "'before'", 'max_length': '20'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.product': {
            'Meta': {'ordering': "['code']", 'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'base_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_product_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_product_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_productcategory_created_by'"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_productcategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.ProductCategory']", 'related_name': "'sub_product_categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.unitofmeasurement': {
            'Meta': {'ordering': "['name']", 'object_name': 'UnitOfMeasurement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_unitofmeasurement_created_by'"}),
            'factor': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_unitofmeasurement_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'rate': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'rounding_precision': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'uom_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UOMCategory']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.uomcategory': {
            'Meta': {'object_name': 'UOMCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_uomcategory_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'core_uomcategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.UOMCategory']", 'related_name': "'core_uomcategory_sub_uom_categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'facilities.facility': {
            'Meta': {'_ormbases': ['core.Company'], 'object_name': 'Facility'},
            'catchment_population': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['core.Company']", 'unique': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'facility_operators': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'blank': 'True', 'related_name': "'facility_operators'", 'to': "orm['core.Company']", 'symmetrical': 'False'}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.FacilityType']"}),
            'global_location_no': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'go_down_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'go_live_date': ('django.db.models.fields.DateField', [], {}),
            'has_electricity': ('django.db.models.fields.BooleanField', [], {}),
            'has_electronic_scc': ('django.db.models.fields.BooleanField', [], {}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_online': ('django.db.models.fields.BooleanField', [], {}),
            'is_satellite': ('django.db.models.fields.BooleanField', [], {}),
            'is_sdp': ('django.db.models.fields.BooleanField', [], {}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Location']"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['facilities.Facility']", 'related_name': "'child_facilities'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'supplies_others': ('django.db.models.fields.BooleanField', [], {}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'virtual_facility': ('django.db.models.fields.BooleanField', [], {})
        },
        'facilities.facilitysupportedprogram': {
            'Meta': {'object_name': 'FacilitySupportedProgram'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'facilities_facilitysupportedprogram_created_by'"}),
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'facilities_facilitysupportedprogram_modified_by'"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.Program']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'facilities.facilitysupportedprogramproduct': {
            'Meta': {'object_name': 'FacilitySupportedProgramProduct'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'buffer_percentage': ('django.db.models.fields.FloatField', [], {}),
            'coverage_rate': ('django.db.models.fields.FloatField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'facilities_facilitysupportedprogramproduct_created_by'"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lead_time': ('django.db.models.fields.IntegerField', [], {}),
            'max_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'min_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'facilities_facilitysupportedprogramproduct_modified_by'"}),
            'order_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.OrderGroup']"}),
            'program_product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.ProgramProduct']"}),
            'push': ('django.db.models.fields.BooleanField', [], {}),
            'supply_interval': ('django.db.models.fields.IntegerField', [], {}),
            'target_population': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'wastage_rate': ('django.db.models.fields.FloatField', [], {}),
            'who_ratio': ('django.db.models.fields.FloatField', [], {})
        },
        'facilities.facilitytype': {
            'Meta': {'object_name': 'FacilityType'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'facilities_facilitytype_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'facilities_facilitytype_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['facilities.FacilityType']", 'related_name': "'sub_facility_types'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'facilities.ordergroup': {
            'Meta': {'object_name': 'OrderGroup'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'facilities_ordergroup_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'member_facilities': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'blank': 'True', 'to': "orm['facilities.Facility']", 'symmetrical': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'facilities_ordergroup_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'supervisory_node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.SupervisoryNode']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'facilities.supervisorynode': {
            'Meta': {'object_name': 'SupervisoryNode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'facilities_supervisorynode_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'facilities_supervisorynode_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['facilities.SupervisoryNode']", 'related_name': "'supervised_nodes'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
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
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'to': "orm['locations.Location']", 'related_name': "'children'"}),
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
        },
        'partners.program': {
            'Meta': {'object_name': 'Program'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'partners_program_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'partners_program_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Company']", 'symmetrical': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'partners.programproduct': {
            'Meta': {'object_name': 'ProgramProduct'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'partners_programproduct_created_by'"}),
            'current_price_per_unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '21', 'decimal_places': '2'}),
            'funding_source': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Company']", 'symmetrical': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'partners_programproduct_modified_by'"}),
            'price_currency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['core.Currency']", 'null': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.Program']"}),
            'unit_per_target': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        }
    }

    complete_apps = ['facilities']