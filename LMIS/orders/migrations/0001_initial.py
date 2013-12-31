# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PurchaseOrder'
        db.create_table('orders_purchaseorder', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_purchaseorder_created_by', to=orm['core.Employee'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_purchaseorder_modified_by', to=orm['core.Employee'])),
            ('purchaser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'], related_name='purchaser')),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'], related_name='purchase_order_supplier')),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('emergency', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order_date', self.gf('django.db.models.fields.DateField')()),
            ('expected_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('orders', ['PurchaseOrder'])

        # Adding model 'PurchaseOrderLine'
        db.create_table('orders_purchaseorderline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_purchaseorderline_created_by', to=orm['core.Employee'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_purchaseorderline_modified_by', to=orm['core.Employee'])),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Program'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Product'])),
            ('quantity_needed', self.gf('django.db.models.fields.IntegerField')()),
            ('current_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'])),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True)),
        ))
        db.send_create_signal('orders', ['PurchaseOrderLine'])

        # Adding model 'SalesOrder'
        db.create_table('orders_salesorder', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_salesorder_created_by', to=orm['core.Employee'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_salesorder_modified_by', to=orm['core.Employee'])),
            ('sales_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.PurchaseOrder'], null=True, blank=True)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'], related_name='recipient')),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'], related_name='sales_order_supplier')),
            ('approved_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Employee'])),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('planned_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('completed_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('orders', ['SalesOrder'])

        # Adding model 'SalesOrderLine'
        db.create_table('orders_salesorderline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_salesorderline_created_by', to=orm['core.Employee'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_salesorderline_modified_by', to=orm['core.Employee'])),
            ('sales_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.SalesOrder'])),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Program'])),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductItem'])),
            ('quantity_requested', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('buffer_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('total_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='sales_quantity_uom')),
            ('total_price', self.gf('django.db.models.fields.DecimalField')(max_digits=21, decimal_places=2)),
            ('price_currency', self.gf('django.db.models.fields.FloatField')()),
            ('total_weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('weight_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='sales_weight_uom')),
            ('total_volume', self.gf('django.db.models.fields.FloatField')()),
            ('vvm_stage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volume_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='sales_volume_uom')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True)),
        ))
        db.send_create_signal('orders', ['SalesOrderLine'])

        # Adding model 'Voucher'
        db.create_table('orders_voucher', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_voucher_created_by', to=orm['core.Employee'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_voucher_modified_by', to=orm['core.Employee'])),
            ('sales_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.SalesOrder'])),
            ('recipient_representative', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Employee'], related_name='recipient_representative')),
            ('supplier_representative', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Employee'], related_name='supplier_representative')),
        ))
        db.send_create_signal('orders', ['Voucher'])

        # Adding model 'VoucherLine'
        db.create_table('orders_voucherline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_voucherline_created_by', to=orm['core.Employee'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, related_name='orders_voucherline_modified_by', to=orm['core.Employee'])),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Program'])),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductItem'])),
            ('input_warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Warehouse'], null=True, blank=True)),
            ('quantity_supplied', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'])),
            ('vvm_stage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True)),
        ))
        db.send_create_signal('orders', ['VoucherLine'])


    def backwards(self, orm):
        # Deleting model 'PurchaseOrder'
        db.delete_table('orders_purchaseorder')

        # Deleting model 'PurchaseOrderLine'
        db.delete_table('orders_purchaseorderline')

        # Deleting model 'SalesOrder'
        db.delete_table('orders_salesorder')

        # Deleting model 'SalesOrderLine'
        db.delete_table('orders_salesorderline')

        # Deleting model 'Voucher'
        db.delete_table('orders_voucher')

        # Deleting model 'VoucherLine'
        db.delete_table('orders_voucherline')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True', 'null': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True', 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_address_created_by'", 'to': "orm['core.Employee']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_address_modified_by'", 'to': "orm['core.Employee']"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True', 'null': 'True'}),
            'subdivision': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True', 'null': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True', 'null': 'True'})
        },
        'core.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Address']", 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Contact']", 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_company_created_by'", 'to': "orm['core.Employee']"}),
            'footer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_company_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Product']", 'null': 'True', 'blank': 'True', 'symmetrical': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_contact_created_by'", 'to': "orm['core.Employee']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'irc': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_contact_modified_by'", 'to': "orm['core.Employee']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'sip': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'core.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_currency_created_by'", 'to': "orm['core.Employee']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_currency_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '5', 'unique': 'True'}),
            'symbol_position': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'before'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Address']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.EmployeeCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Contact']", 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_employee_created_by'", 'to': "orm['core.Employee']"}),
            'current_company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Company']", 'related_name': "'employees'"}),
            'main_company': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_employee_main_company_employees'", 'to': "orm['core.Company']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_employee_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.employeecategory': {
            'Meta': {'object_name': 'EmployeeCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_employeecategory_created_by'", 'to': "orm['core.Employee']"}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_employeecategory_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_employeecategory_sub_employee_categories'", 'to': "orm['core.EmployeeCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.facility': {
            'Meta': {'object_name': 'Facility', '_ormbases': ['core.Company']},
            'catchment_population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['core.Company']", 'unique': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'facility_operators': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'null': 'True', 'related_name': "'facility_operators'", 'symmetrical': 'False', 'to': "orm['core.Company']"}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.FacilityType']"}),
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
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'child_facilities'", 'to': "orm['core.Facility']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'sdp': ('django.db.models.fields.BooleanField', [], {}),
            'supplies_others': ('django.db.models.fields.BooleanField', [], {}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'virtual_facility': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.facilitytype': {
            'Meta': {'object_name': 'FacilityType'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_facilitytype_created_by'", 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_facilitytype_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'sub_facility_types'", 'to': "orm['core.FacilityType']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.modeofadministration': {
            'Meta': {'object_name': 'ModeOfAdministration'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_modeofadministration_created_by'", 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_modeofadministration_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'base_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_product_created_by'", 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_product_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_productcategory_created_by'", 'to': "orm['core.Employee']"}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_productcategory_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'sub_product_categories'", 'to': "orm['core.ProductCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.productitem': {
            'Meta': {'object_name': 'ProductItem'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'country_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_productitem_created_by'", 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {}),
            'gtin': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Company']"}),
            'mode_of_use': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ModeOfAdministration']", 'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_productitem_modified_by'", 'to': "orm['core.Employee']"}),
            'moh_bar_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductPresentation']"}),
            'price_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Currency']", 'null': 'True', 'blank': 'True'}),
            'price_per_unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '21', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'product_batch_no': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'volume_per_unit': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'product_item_volume_uom'", 'to': "orm['core.UnitOfMeasurement']"}),
            'weight_per_unit': ('django.db.models.fields.FloatField', [], {'max_length': '21', 'blank': 'True', 'null': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'product_item_weight_uom'", 'to': "orm['core.UnitOfMeasurement']"})
        },
        'core.productpresentation': {
            'Meta': {'object_name': 'ProductPresentation'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_productpresentation_created_by'", 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_productpresentation_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.program': {
            'Meta': {'object_name': 'Program'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_program_created_by'", 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_program_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Company']", 'symmetrical': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.unitofmeasurement': {
            'Meta': {'object_name': 'UnitOfMeasurement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_unitofmeasurement_created_by'", 'to': "orm['core.Employee']"}),
            'factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_unitofmeasurement_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rounding_precision': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True', 'null': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uom_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UOMCategory']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.uomcategory': {
            'Meta': {'object_name': 'UOMCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_uomcategory_created_by'", 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_uomcategory_modified_by'", 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_uomcategory_sub_uom_categories'", 'to': "orm['core.UOMCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'ambient_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ambient_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'cold_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cold_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_warehouse_created_by'", 'to': "orm['core.Employee']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'is_refrigerated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'core_warehouse_modified_by'", 'to': "orm['core.Employee']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'alt_names': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.LocationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'Unknown'"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['locations.Location']", 'null': 'True', 'related_name': "'children'"}),
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
        },
        'orders.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_purchaseorder_created_by'", 'to': "orm['core.Employee']"}),
            'emergency': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expected_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_purchaseorder_modified_by'", 'to': "orm['core.Employee']"}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'purchaser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']", 'related_name': "'purchaser'"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']", 'related_name': "'purchase_order_supplier'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'orders.purchaseorderline': {
            'Meta': {'object_name': 'PurchaseOrderLine'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_purchaseorderline_created_by'", 'to': "orm['core.Employee']"}),
            'current_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_purchaseorderline_modified_by'", 'to': "orm['core.Employee']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Program']"}),
            'quantity_needed': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'orders.salesorder': {
            'Meta': {'object_name': 'SalesOrder'},
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']"}),
            'completed_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_salesorder_created_by'", 'to': "orm['core.Employee']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_salesorder_modified_by'", 'to': "orm['core.Employee']"}),
            'planned_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']", 'related_name': "'recipient'"}),
            'sales_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.PurchaseOrder']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']", 'related_name': "'sales_order_supplier'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'orders.salesorderline': {
            'Meta': {'object_name': 'SalesOrderLine'},
            'buffer_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_salesorderline_created_by'", 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_salesorderline_modified_by'", 'to': "orm['core.Employee']"}),
            'price_currency': ('django.db.models.fields.FloatField', [], {}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Program']"}),
            'quantity_requested': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'sales_quantity_uom'"}),
            'sales_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.SalesOrder']"}),
            'total_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '21', 'decimal_places': '2'}),
            'total_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'total_volume': ('django.db.models.fields.FloatField', [], {}),
            'total_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'sales_volume_uom'"}),
            'vvm_stage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'sales_weight_uom'"})
        },
        'orders.voucher': {
            'Meta': {'object_name': 'Voucher'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_voucher_created_by'", 'to': "orm['core.Employee']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_voucher_modified_by'", 'to': "orm['core.Employee']"}),
            'recipient_representative': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']", 'related_name': "'recipient_representative'"}),
            'sales_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.SalesOrder']"}),
            'supplier_representative': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']", 'related_name': "'supplier_representative'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'orders.voucherline': {
            'Meta': {'object_name': 'VoucherLine'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_voucherline_created_by'", 'to': "orm['core.Employee']"}),
            'input_warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Warehouse']", 'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'orders_voucherline_modified_by'", 'to': "orm['core.Employee']"}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Program']"}),
            'quantity_supplied': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'vvm_stage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['orders']