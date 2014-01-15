# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ConsumptionRecordLineAdjustment'
        db.create_table('inventory_consumptionrecordlineadjustment', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventory_consumptionrecordlineadjustment_created_by', to=orm['auth.User'], null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventory_consumptionrecordlineadjustment_modified_by', to=orm['auth.User'], null=True, blank=True)),
            ('consumption_record_line', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.ConsumptionRecordLine'])),
            ('adjustment', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventory.Adjustment'], unique=True)),
        ))
        db.send_create_signal('inventory', ['ConsumptionRecordLineAdjustment'])

        # Deleting field 'ConsumptionRecordLine.quantity_dispensed'
        db.delete_column('inventory_consumptionrecordline', 'quantity_dispensed')

        # Adding field 'ConsumptionRecordLine.previous_balance'
        db.add_column('inventory_consumptionrecordline', 'previous_balance',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'ConsumptionRecordLine.quantity_used'
        db.add_column('inventory_consumptionrecordline', 'quantity_used',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'ConsumptionRecordLine.current_balance'
        db.add_column('inventory_consumptionrecordline', 'current_balance',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'ConsumptionRecordLine.quantity_received'
        db.add_column('inventory_consumptionrecordline', 'quantity_received',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'ConsumptionRecordLine.total_discarded'
        db.add_column('inventory_consumptionrecordline', 'total_discarded',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ConsumptionRecordLineAdjustment'
        db.delete_table('inventory_consumptionrecordlineadjustment')

        # Adding field 'ConsumptionRecordLine.quantity_dispensed'
        db.add_column('inventory_consumptionrecordline', 'quantity_dispensed',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'ConsumptionRecordLine.previous_balance'
        db.delete_column('inventory_consumptionrecordline', 'previous_balance')

        # Deleting field 'ConsumptionRecordLine.quantity_used'
        db.delete_column('inventory_consumptionrecordline', 'quantity_used')

        # Deleting field 'ConsumptionRecordLine.current_balance'
        db.delete_column('inventory_consumptionrecordline', 'current_balance')

        # Deleting field 'ConsumptionRecordLine.quantity_received'
        db.delete_column('inventory_consumptionrecordline', 'quantity_received')

        # Deleting field 'ConsumptionRecordLine.total_discarded'
        db.delete_column('inventory_consumptionrecordline', 'total_discarded')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cce.coldchainequipment': {
            'Meta': {'object_name': 'ColdChainEquipment'},
            'capacity_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_coldchainequipment_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_coldchainequipment_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'storage_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Warehouse']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cce.ColdChainEquipmentType']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'cce.coldchainequipmenttype': {
            'Meta': {'object_name': 'ColdChainEquipmentType'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_coldchainequipmenttype_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'maximum_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_coldchainequipmenttype_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'temperature_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '35', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '5', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_address_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_address_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '35', 'blank': 'True'}),
            'subdivision': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '35', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '15', 'blank': 'True'})
        },
        'core.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Address']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.CompanyCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Contact']", 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_company_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'footer': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_company_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Product']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_companycategory_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_companycategory_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'core_companycategory_sub_company_categories'", 'to': "orm['core.CompanyCategory']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_contact_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'irc': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_contact_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'sip': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'core.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_currency_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_currency_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'symbol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'symbol_position': ('django.db.models.fields.CharField', [], {'default': "'before'", 'max_length': '20'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Address']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.EmployeeCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Contact']", 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_employee_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'current_company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'employees'", 'to': "orm['core.Company']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'main_company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_employee_main_company_employees'", 'to': "orm['core.Company']", 'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_employee_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'null': 'True', 'unique': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.employeecategory': {
            'Meta': {'object_name': 'EmployeeCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_employeecategory_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_employeecategory_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'core_employeecategory_sub_employee_categories'", 'to': "orm['core.EmployeeCategory']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.modeofadministration': {
            'Meta': {'object_name': 'ModeOfAdministration'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_modeofadministration_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_modeofadministration_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'base_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_product_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_product_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_productcategory_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_productcategory_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'sub_product_categories'", 'to': "orm['core.ProductCategory']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.productitem': {
            'Meta': {'object_name': 'ProductItem'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'country_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_productitem_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {}),
            'gtin': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Company']"}),
            'mode_of_use': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ModeOfAdministration']", 'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_productitem_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'moh_bar_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductPresentation']"}),
            'price_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Currency']", 'null': 'True', 'blank': 'True'}),
            'price_per_unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '21', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'product_batch_no': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'volume_per_unit': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product_item_volume_uom'", 'to': "orm['core.UnitOfMeasurement']", 'null': 'True', 'blank': 'True'}),
            'weight_per_unit': ('django.db.models.fields.FloatField', [], {'null': 'True', 'max_length': '21', 'blank': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product_item_weight_uom'", 'to': "orm['core.UnitOfMeasurement']", 'null': 'True', 'blank': 'True'})
        },
        'core.productpresentation': {
            'Meta': {'object_name': 'ProductPresentation'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_productpresentation_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_productpresentation_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.program': {
            'Meta': {'object_name': 'Program'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_program_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_program_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Company']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.unitofmeasurement': {
            'Meta': {'object_name': 'UnitOfMeasurement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_unitofmeasurement_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_unitofmeasurement_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rounding_precision': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uom_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UOMCategory']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.uomcategory': {
            'Meta': {'object_name': 'UOMCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_uomcategory_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_uomcategory_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'core_uomcategory_sub_uom_categories'", 'to': "orm['core.UOMCategory']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'facilities.facility': {
            'Meta': {'object_name': 'Facility', '_ormbases': ['core.Company']},
            'catchment_population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Company']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'facility_operators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'facility_operators'", 'null': 'True', 'to': "orm['core.Company']", 'blank': 'True'}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.FacilityType']"}),
            'global_location_no': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'go_down_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'go_live_date': ('django.db.models.fields.DateField', [], {}),
            'has_electricity': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_electronic_dar': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_electronic_scc': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'is_online': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_satellite': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Location']", 'null': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'child_facilities'", 'to': "orm['facilities.Facility']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'sdp': ('django.db.models.fields.BooleanField', [], {}),
            'supplies_others': ('django.db.models.fields.BooleanField', [], {}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'virtual_facility': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'facilities.facilitytype': {
            'Meta': {'object_name': 'FacilityType'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facilities_facilitytype_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facilities_facilitytype_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'sub_facility_types'", 'to': "orm['facilities.FacilityType']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'facilities.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'ambient_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ambient_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'cold_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cold_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facilities_warehouse_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_refrigerated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facilities_warehouse_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.adjustment': {
            'Meta': {'object_name': 'Adjustment'},
            'adjustment_type': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_adjustment_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_adjustment_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'previous_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'revised_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.adjustmenttype': {
            'Meta': {'object_name': 'AdjustmentType', 'managed': 'False'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_adjustmenttype_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_adjustmenttype_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.consumptionrecord': {
            'Meta': {'object_name': 'ConsumptionRecord'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_consumptionrecord_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_consumptionrecord_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'performed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'verified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_consumptionrecord_verifier'", 'to': "orm['core.Employee']"})
        },
        'inventory.consumptionrecordline': {
            'Meta': {'object_name': 'ConsumptionRecordLine'},
            'consumption_record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.ConsumptionRecord']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_consumptionrecordline_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'current_balance': ('django.db.models.fields.IntegerField', [], {}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_consumptionrecordline_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'previous_balance': ('django.db.models.fields.IntegerField', [], {}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Program']"}),
            'quantity_received': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'quantity_used': ('django.db.models.fields.IntegerField', [], {}),
            'total_discarded': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.consumptionrecordlineadjustment': {
            'Meta': {'object_name': 'ConsumptionRecordLineAdjustment'},
            'adjustment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['inventory.Adjustment']", 'unique': 'True'}),
            'consumption_record_line': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.ConsumptionRecordLine']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_consumptionrecordlineadjustment_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_consumptionrecordlineadjustment_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.incomingshipment': {
            'Meta': {'object_name': 'IncomingShipment'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_incomingshipment_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'input_warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Warehouse']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_incomingshipment_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'other_source': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'others': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stock_entry_type': ('django.db.models.fields.IntegerField', [], {}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.incomingshipmentline': {
            'Meta': {'object_name': 'IncomingShipmentLine'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_incomingshipmentline_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_incomingshipmentline_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'packed_volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'packed_volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_incomingshipmentline_packed_volume_uom'", 'to': "orm['core.UnitOfMeasurement']"}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_incomingshipmentline_quantity_uom'", 'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'voucher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Voucher']", 'null': 'True', 'blank': 'True'}),
            'vvm_stage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_incomingshipmentline_weight_uom'", 'to': "orm['core.UnitOfMeasurement']"})
        },
        'inventory.inventory': {
            'Meta': {'object_name': 'Inventory'},
            'cce': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cce.ColdChainEquipment']", 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_inventory_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_inventory_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Warehouse']"})
        },
        'inventory.inventoryline': {
            'Meta': {'object_name': 'InventoryLine'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_inventoryline_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory'", 'to': "orm['inventory.Inventory']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_inventoryline_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Program']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_inventoryline_volume_uom'", 'to': "orm['core.UnitOfMeasurement']", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_inventoryline_weight_uom'", 'to': "orm['core.UnitOfMeasurement']", 'null': 'True', 'blank': 'True'})
        },
        'inventory.inventorylineadjustment': {
            'Meta': {'object_name': 'InventoryLineAdjustment'},
            'adjustment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['inventory.Adjustment']", 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_inventorylineadjustment_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'inventory_line': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.InventoryLine']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_inventorylineadjustment_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.outgoingshipment': {
            'Meta': {'object_name': 'OutgoingShipment'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_outgoingshipment_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_outgoingshipment_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'output_warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Warehouse']"}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.outgoingshipmentline': {
            'Meta': {'object_name': 'OutgoingShipmentLine'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_outgoingshipmentline_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_outgoingshipmentline_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity_after': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_before': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_issued': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_outgoingshipmentline_quantity_uom'", 'to': "orm['core.UnitOfMeasurement']"}),
            'remark': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '55', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_outgoingshipmentline_volume_uom'", 'to': "orm['core.UnitOfMeasurement']", 'null': 'True', 'blank': 'True'}),
            'weight_issued': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_outgoingshipmentline_weight_uom'", 'to': "orm['core.UnitOfMeasurement']", 'null': 'True', 'blank': 'True'})
        },
        'inventory.physicalstockcount': {
            'Meta': {'object_name': 'PhysicalStockCount'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_physicalstockcount_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_physicalstockcount_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'performed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'verified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_physicalstockcount_verifier'", 'to': "orm['core.Employee']"})
        },
        'inventory.physicalstockcountline': {
            'Meta': {'object_name': 'PhysicalStockCountLine'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_physicalstockcountline_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'inventory_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_physicalstockcountline_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'physical_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'physical_stock_count': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.PhysicalStockCount']"}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Program']"}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_physicalstockcountline_quantity_uom'", 'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'vvm_stage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'inventory.physicalstockcountlineadjustment': {
            'Meta': {'object_name': 'PhysicalStockCountLineAdjustment'},
            'adjustment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['inventory.Adjustment']", 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_physicalstockcountlineadjustment_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_physicalstockcountlineadjustment_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'physical_stock_line': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.PhysicalStockCountLine']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.stockentry': {
            'Meta': {'object_name': 'StockEntry', 'managed': 'False'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_stockentry_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_stockentry_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'alt_names': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.LocationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'children'", 'to': "orm['locations.Location']", 'null': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'locations.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'code': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'})
        },
        'orders.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_purchaseorder_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'emergency': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expected_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_purchaseorder_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'purchaser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_purchaseorder_purchaser'", 'to': "orm['facilities.Facility']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_purchaseorder_supplier'", 'to': "orm['facilities.Facility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'orders.salesorder': {
            'Meta': {'object_name': 'SalesOrder'},
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']"}),
            'completed_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_salesorder_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_salesorder_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'planned_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_salesorder_recipient'", 'to': "orm['facilities.Facility']"}),
            'sales_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.PurchaseOrder']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_salesorder_supplier'", 'to': "orm['facilities.Facility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'orders.voucher': {
            'Meta': {'object_name': 'Voucher'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_voucher_created_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_voucher_modified_by'", 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'recipient_representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_voucher_recipient_representative'", 'to': "orm['core.Employee']"}),
            'sales_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.SalesOrder']"}),
            'supplier_representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_voucher_supplier_representative'", 'to': "orm['core.Employee']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        }
    }

    complete_apps = ['inventory']