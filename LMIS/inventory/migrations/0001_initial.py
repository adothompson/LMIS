# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Inventory'
        db.create_table('inventory_inventory', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_inventory_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_inventory_modified_by')),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Warehouse'])),
            ('cce', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['cce.ColdChainEquipment'], blank=True)),
        ))
        db.send_create_signal('inventory', ['Inventory'])

        # Adding model 'InventoryLine'
        db.create_table('inventory_inventoryline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_inventoryline_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_inventoryline_modified_by')),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductItem'])),
            ('inventory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Inventory'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('weight_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.UnitOfMeasurement'], blank=True, related_name='inventory_inventoryline_weight_uom')),
            ('volume', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('volume_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.UnitOfMeasurement'], blank=True, related_name='inventory_inventoryline_volume_uom')),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('inventory', ['InventoryLine'])

        # Adding model 'PhysicalStockCount'
        db.create_table('inventory_physicalstockcount', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_physicalstockcount_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_physicalstockcount_modified_by')),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'])),
            ('performed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Employee'])),
            ('verified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Employee'], related_name='inventory_physicalstockcount_verifier')),
        ))
        db.send_create_signal('inventory', ['PhysicalStockCount'])

        # Adding model 'PhysicalStockCountLine'
        db.create_table('inventory_physicalstockcountline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_physicalstockcountline_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_physicalstockcountline_modified_by')),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductItem'])),
            ('physical_stock_count', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.PhysicalStockCount'])),
            ('physical_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('inventory_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='inventory_physicalstockcountline_quantity_uom')),
            ('vvm_stage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
        ))
        db.send_create_signal('inventory', ['PhysicalStockCountLine'])

        # Adding model 'ConsumptionRecord'
        db.create_table('inventory_consumptionrecord', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_consumptionrecord_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_consumptionrecord_modified_by')),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'])),
            ('performed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Employee'])),
            ('verified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Employee'], related_name='inventory_consumptionrecord_verifier')),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('inventory', ['ConsumptionRecord'])

        # Adding model 'ConsumptionRecordLine'
        db.create_table('inventory_consumptionrecordline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_consumptionrecordline_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_consumptionrecordline_modified_by')),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductItem'])),
            ('consumption_record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.ConsumptionRecord'])),
            ('quantity_dispensed', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'])),
        ))
        db.send_create_signal('inventory', ['ConsumptionRecordLine'])

        # Adding model 'IncomingShipment'
        db.create_table('inventory_incomingshipment', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_incomingshipment_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_incomingshipment_modified_by')),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'])),
            ('stock_entry_type', self.gf('django.db.models.fields.IntegerField')()),
            ('input_warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Warehouse'])),
            ('others', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('other_source', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
        ))
        db.send_create_signal('inventory', ['IncomingShipment'])

        # Adding model 'IncomingShipmentLine'
        db.create_table('inventory_incomingshipmentline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_incomingshipmentline_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_incomingshipmentline_modified_by')),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductItem'])),
            ('quantity_received', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='inventory_incomingshipmentline_quantity_uom')),
            ('stock_before', self.gf('django.db.models.fields.IntegerField')()),
            ('stock_after', self.gf('django.db.models.fields.IntegerField')()),
            ('stock_balance', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('stock_balance_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.UnitOfMeasurement'], blank=True, related_name='inventory_incomingshipmentline_stock_balance_uom')),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('weight_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='weight_uom')),
            ('packed_volume', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('packed_volume_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='inventory_incomingshipmentline_packed_volume_uom')),
            ('vvm_stage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voucher', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['orders.Voucher'], blank=True)),
        ))
        db.send_create_signal('inventory', ['IncomingShipmentLine'])

        # Adding model 'OutgoingShipment'
        db.create_table('inventory_outgoingshipment', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_outgoingshipment_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_outgoingshipment_modified_by')),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'])),
            ('stock_entry_type', self.gf('django.db.models.fields.IntegerField')()),
            ('output_warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Warehouse'])),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('inventory', ['OutgoingShipment'])

        # Adding model 'OutgoingShipmentLine'
        db.create_table('inventory_outgoingshipmentline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_outgoingshipmentline_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_outgoingshipmentline_modified_by')),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductItem'])),
            ('quantity_issued', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='inventory_outgoingshipmentline_quantity_uom')),
            ('weight_issued', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('weight_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.UnitOfMeasurement'], blank=True, related_name='inventory_outgoingshipmentline_weight_uom')),
            ('volume', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('volume_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.UnitOfMeasurement'], blank=True, related_name='inventory_outgoingshipmentline_volume_uom')),
            ('stock_before', self.gf('django.db.models.fields.IntegerField')()),
            ('stock_after', self.gf('django.db.models.fields.IntegerField')()),
            ('stock_balance', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('stock_balance_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.UnitOfMeasurement'], blank=True, related_name='inventory_outgoingshipmentline_stock_balance_uom')),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=55, null=True, blank=True)),
        ))
        db.send_create_signal('inventory', ['OutgoingShipmentLine'])

        # Adding model 'Adjustment'
        db.create_table('inventory_adjustment', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_adjustment_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Employee'], blank=True, related_name='inventory_adjustment_modified_by')),
            ('physical_stock_line', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.PhysicalStockCountLine'])),
            ('previous_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('revised_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('inventory', ['Adjustment'])


    def backwards(self, orm):
        # Deleting model 'Inventory'
        db.delete_table('inventory_inventory')

        # Deleting model 'InventoryLine'
        db.delete_table('inventory_inventoryline')

        # Deleting model 'PhysicalStockCount'
        db.delete_table('inventory_physicalstockcount')

        # Deleting model 'PhysicalStockCountLine'
        db.delete_table('inventory_physicalstockcountline')

        # Deleting model 'ConsumptionRecord'
        db.delete_table('inventory_consumptionrecord')

        # Deleting model 'ConsumptionRecordLine'
        db.delete_table('inventory_consumptionrecordline')

        # Deleting model 'IncomingShipment'
        db.delete_table('inventory_incomingshipment')

        # Deleting model 'IncomingShipmentLine'
        db.delete_table('inventory_incomingshipmentline')

        # Deleting model 'OutgoingShipment'
        db.delete_table('inventory_outgoingshipment')

        # Deleting model 'OutgoingShipmentLine'
        db.delete_table('inventory_outgoingshipmentline')

        # Deleting model 'Adjustment'
        db.delete_table('inventory_adjustment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'cce.coldchainequipment': {
            'Meta': {'object_name': 'ColdChainEquipment'},
            'capacity_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.UnitOfMeasurement']", 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'cce_coldchainequipment_created_by'"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'cce_coldchainequipment_modified_by'"}),
            'net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'storage_location': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Warehouse']", 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cce.ColdChainEquipmentType']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'cce.coldchainequipmenttype': {
            'Meta': {'object_name': 'ColdChainEquipmentType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'cce_coldchainequipmenttype_created_by'"}),
            'maximum_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'cce_coldchainequipmenttype_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'temperature_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.UnitOfMeasurement']", 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_address_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_address_modified_by'"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'subdivision': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        'core.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Address']", 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Contact']", 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_company_created_by'"}),
            'footer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_company_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['core.Product']", 'blank': 'True', 'symmetrical': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_contact_created_by'"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'irc': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_contact_modified_by'"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_currency_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_currency_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '5', 'unique': 'True'}),
            'symbol_position': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'before'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Address']", 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.EmployeeCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Contact']", 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_employee_created_by'"}),
            'current_company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Company']", 'related_name': "'employees'"}),
            'main_company': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Company']", 'blank': 'True', 'related_name': "'core_employee_main_company_employees'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_employee_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.employeecategory': {
            'Meta': {'object_name': 'EmployeeCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_employeecategory_created_by'"}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_employeecategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'to': "orm['core.EmployeeCategory']", 'blank': 'True', 'related_name': "'core_employeecategory_sub_employee_categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.facility': {
            'Meta': {'object_name': 'Facility', '_ormbases': ['core.Company']},
            'catchment_population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Company']", 'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'facility_operators': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['core.Company']", 'related_name': "'facility_operators'", 'blank': 'True', 'symmetrical': 'False'}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.FacilityType']"}),
            'global_location_no': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'go_down_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'go_live_date': ('django.db.models.fields.DateField', [], {}),
            'has_electricity': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_electronic_dar': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_electronic_scc': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'default': 'True', 'blank': 'True'}),
            'is_online': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_satellite': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['locations.Location']"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'to': "orm['core.Facility']", 'blank': 'True', 'related_name': "'child_facilities'"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_facilitytype_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_facilitytype_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'to': "orm['core.FacilityType']", 'blank': 'True', 'related_name': "'sub_facility_types'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.modeofadministration': {
            'Meta': {'object_name': 'ModeOfAdministration'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_modeofadministration_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_modeofadministration_modified_by'"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_product_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_product_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_productcategory_created_by'"}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_productcategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'to': "orm['core.ProductCategory']", 'blank': 'True', 'related_name': "'sub_product_categories'"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_productitem_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {}),
            'gtin': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Company']"}),
            'mode_of_use': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.ModeOfAdministration']", 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_productitem_modified_by'"}),
            'moh_bar_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductPresentation']"}),
            'price_currency': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Currency']", 'blank': 'True'}),
            'price_per_unit': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '21'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'product_batch_no': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'volume_per_unit': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.UnitOfMeasurement']", 'blank': 'True', 'related_name': "'product_item_volume_uom'"}),
            'weight_per_unit': ('django.db.models.fields.FloatField', [], {'max_length': '21', 'null': 'True', 'blank': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.UnitOfMeasurement']", 'blank': 'True', 'related_name': "'product_item_weight_uom'"})
        },
        'core.productpresentation': {
            'Meta': {'object_name': 'ProductPresentation'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_productpresentation_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_productpresentation_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.unitofmeasurement': {
            'Meta': {'object_name': 'UnitOfMeasurement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_unitofmeasurement_created_by'"}),
            'factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_unitofmeasurement_modified_by'"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_uomcategory_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_uomcategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'to': "orm['core.UOMCategory']", 'blank': 'True', 'related_name': "'core_uomcategory_sub_uom_categories'"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_warehouse_created_by'"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'is_refrigerated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'core_warehouse_modified_by'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.adjustment': {
            'Meta': {'object_name': 'Adjustment'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_adjustment_created_by'"}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_adjustment_modified_by'"}),
            'physical_stock_line': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.PhysicalStockCountLine']"}),
            'previous_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'revised_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.consumptionrecord': {
            'Meta': {'object_name': 'ConsumptionRecord'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_consumptionrecord_created_by'"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_consumptionrecord_modified_by'"}),
            'performed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'verified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']", 'related_name': "'inventory_consumptionrecord_verifier'"})
        },
        'inventory.consumptionrecordline': {
            'Meta': {'object_name': 'ConsumptionRecordLine'},
            'consumption_record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.ConsumptionRecord']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_consumptionrecordline_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_consumptionrecordline_modified_by'"}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity_dispensed': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.incomingshipment': {
            'Meta': {'object_name': 'IncomingShipment'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_incomingshipment_created_by'"}),
            'input_warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Warehouse']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_incomingshipment_modified_by'"}),
            'other_source': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'others': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stock_entry_type': ('django.db.models.fields.IntegerField', [], {}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.incomingshipmentline': {
            'Meta': {'object_name': 'IncomingShipmentLine'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_incomingshipmentline_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_incomingshipmentline_modified_by'"}),
            'packed_volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'packed_volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'inventory_incomingshipmentline_packed_volume_uom'"}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity_received': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'inventory_incomingshipmentline_quantity_uom'"}),
            'stock_after': ('django.db.models.fields.IntegerField', [], {}),
            'stock_balance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stock_balance_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.UnitOfMeasurement']", 'blank': 'True', 'related_name': "'inventory_incomingshipmentline_stock_balance_uom'"}),
            'stock_before': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'voucher': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['orders.Voucher']", 'blank': 'True'}),
            'vvm_stage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'weight_uom'"})
        },
        'inventory.inventory': {
            'Meta': {'object_name': 'Inventory'},
            'cce': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['cce.ColdChainEquipment']", 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_inventory_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_inventory_modified_by'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Warehouse']"})
        },
        'inventory.inventoryline': {
            'Meta': {'object_name': 'InventoryLine'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_inventoryline_created_by'"}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.Inventory']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_inventoryline_modified_by'"}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.UnitOfMeasurement']", 'blank': 'True', 'related_name': "'inventory_inventoryline_volume_uom'"}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.UnitOfMeasurement']", 'blank': 'True', 'related_name': "'inventory_inventoryline_weight_uom'"})
        },
        'inventory.outgoingshipment': {
            'Meta': {'object_name': 'OutgoingShipment'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_outgoingshipment_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_outgoingshipment_modified_by'"}),
            'output_warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Warehouse']"}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'stock_entry_type': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'inventory.outgoingshipmentline': {
            'Meta': {'object_name': 'OutgoingShipmentLine'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_outgoingshipmentline_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_outgoingshipmentline_modified_by'"}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity_issued': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'inventory_outgoingshipmentline_quantity_uom'"}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '55', 'null': 'True', 'blank': 'True'}),
            'stock_after': ('django.db.models.fields.IntegerField', [], {}),
            'stock_balance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stock_balance_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.UnitOfMeasurement']", 'blank': 'True', 'related_name': "'inventory_outgoingshipmentline_stock_balance_uom'"}),
            'stock_before': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.UnitOfMeasurement']", 'blank': 'True', 'related_name': "'inventory_outgoingshipmentline_volume_uom'"}),
            'weight_issued': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.UnitOfMeasurement']", 'blank': 'True', 'related_name': "'inventory_outgoingshipmentline_weight_uom'"})
        },
        'inventory.physicalstockcount': {
            'Meta': {'object_name': 'PhysicalStockCount'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_physicalstockcount_created_by'"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_physicalstockcount_modified_by'"}),
            'performed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'verified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']", 'related_name': "'inventory_physicalstockcount_verifier'"})
        },
        'inventory.physicalstockcountline': {
            'Meta': {'object_name': 'PhysicalStockCountLine'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_physicalstockcountline_created_by'"}),
            'inventory_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_physicalstockcountline_modified_by'"}),
            'physical_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'physical_stock_count': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.PhysicalStockCount']"}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'inventory_physicalstockcountline_quantity_uom'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'vvm_stage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'inventory.stockentry': {
            'Meta': {'object_name': 'StockEntry', 'managed': 'False'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_stockentry_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'inventory_stockentry_modified_by'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'alt_names': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.LocationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'Unknown'"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'to': "orm['locations.Location']", 'related_name': "'children'"}),
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
        },
        'orders.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'orders_purchaseorder_created_by'"}),
            'emergency': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expected_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'orders_purchaseorder_modified_by'"}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'purchaser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']", 'related_name': "'purchaser'"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']", 'related_name': "'purchase_order_supplier'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'orders.salesorder': {
            'Meta': {'object_name': 'SalesOrder'},
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']"}),
            'completed_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'orders_salesorder_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'orders_salesorder_modified_by'"}),
            'planned_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']", 'related_name': "'recipient'"}),
            'sales_order': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['orders.PurchaseOrder']", 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']", 'related_name': "'sales_order_supplier'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'orders.voucher': {
            'Meta': {'object_name': 'Voucher'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'orders_voucher_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['core.Employee']", 'blank': 'True', 'related_name': "'orders_voucher_modified_by'"}),
            'recipient_representative': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']", 'related_name': "'recipient_representative'"}),
            'sales_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.SalesOrder']"}),
            'supplier_representative': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']", 'related_name': "'supplier_representative'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        }
    }

    complete_apps = ['inventory']