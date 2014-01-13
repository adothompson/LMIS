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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_inventory_created_by', null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_inventory_modified_by', null=True, blank=True)),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Warehouse'])),
            ('cce', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, to=orm['cce.ColdChainEquipment'])),
        ))
        db.send_create_signal('inventory', ['Inventory'])

        # Adding model 'InventoryLine'
        db.create_table('inventory_inventoryline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_inventoryline_created_by', null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_inventoryline_modified_by', null=True, blank=True)),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductItem'])),
            ('inventory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Inventory'])),
            ('adjustments', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, to=orm['inventory.Adjustment'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('weight_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='inventory_inventoryline_weight_uom', null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('volume_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='inventory_inventoryline_volume_uom', null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('inventory', ['InventoryLine'])

        # Adding model 'PhysicalStockCount'
        db.create_table('inventory_physicalstockcount', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_physicalstockcount_created_by', null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_physicalstockcount_modified_by', null=True, blank=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('performed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Employee'])),
            ('verified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventory_physicalstockcount_verifier', to=orm['core.Employee'])),
        ))
        db.send_create_signal('inventory', ['PhysicalStockCount'])

        # Adding model 'PhysicalStockCountLine'
        db.create_table('inventory_physicalstockcountline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_physicalstockcountline_created_by', null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_physicalstockcountline_modified_by', null=True, blank=True)),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductItem'])),
            ('physical_stock_count', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.PhysicalStockCount'])),
            ('physical_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('inventory_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_uom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventory_physicalstockcountline_quantity_uom', to=orm['core.UnitOfMeasurement'])),
            ('vvm_stage', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(blank=True, max_length=35)),
        ))
        db.send_create_signal('inventory', ['PhysicalStockCountLine'])

        # Adding model 'ConsumptionRecord'
        db.create_table('inventory_consumptionrecord', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_consumptionrecord_created_by', null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_consumptionrecord_modified_by', null=True, blank=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('performed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Employee'])),
            ('verified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventory_consumptionrecord_verifier', to=orm['core.Employee'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('inventory', ['ConsumptionRecord'])

        # Adding model 'ConsumptionRecordLine'
        db.create_table('inventory_consumptionrecordline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_consumptionrecordline_created_by', null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_consumptionrecordline_modified_by', null=True, blank=True)),
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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_incomingshipment_created_by', null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_incomingshipment_modified_by', null=True, blank=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('stock_entry_type', self.gf('django.db.models.fields.IntegerField')()),
            ('input_warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Warehouse'])),
            ('others', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('other_source', self.gf('django.db.models.fields.CharField')(blank=True, max_length=35)),
        ))
        db.send_create_signal('inventory', ['IncomingShipment'])

        # Adding model 'IncomingShipmentLine'
        db.create_table('inventory_incomingshipmentline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_incomingshipmentline_created_by', null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_incomingshipmentline_modified_by', null=True, blank=True)),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductItem'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_uom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventory_incomingshipmentline_quantity_uom', to=orm['core.UnitOfMeasurement'])),
            ('weight', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('weight_uom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventory_incomingshipmentline_weight_uom', to=orm['core.UnitOfMeasurement'])),
            ('packed_volume', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('packed_volume_uom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventory_incomingshipmentline_packed_volume_uom', to=orm['core.UnitOfMeasurement'])),
            ('vvm_stage', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('voucher', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, to=orm['orders.Voucher'])),
        ))
        db.send_create_signal('inventory', ['IncomingShipmentLine'])

        # Adding model 'OutgoingShipment'
        db.create_table('inventory_outgoingshipment', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_outgoingshipment_created_by', null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_outgoingshipment_modified_by', null=True, blank=True)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('stock_entry_type', self.gf('django.db.models.fields.IntegerField')()),
            ('output_warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Warehouse'])),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('inventory', ['OutgoingShipment'])

        # Adding model 'OutgoingShipmentLine'
        db.create_table('inventory_outgoingshipmentline', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_outgoingshipmentline_created_by', null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_outgoingshipmentline_modified_by', null=True, blank=True)),
            ('product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductItem'])),
            ('quantity_issued', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_uom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventory_outgoingshipmentline_quantity_uom', to=orm['core.UnitOfMeasurement'])),
            ('weight_issued', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('weight_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='inventory_outgoingshipmentline_weight_uom', null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('volume_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'], related_name='inventory_outgoingshipmentline_volume_uom', null=True, blank=True)),
            ('quantity_before', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_after', self.gf('django.db.models.fields.IntegerField')()),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True, null=True)),
        ))
        db.send_create_signal('inventory', ['OutgoingShipmentLine'])

        # Adding model 'Adjustment'
        db.create_table('inventory_adjustment', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_adjustment_created_by', null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='inventory_adjustment_modified_by', null=True, blank=True)),
            ('physical_stock_line', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.PhysicalStockCountLine'])),
            ('previous_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('revised_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('adjustment_type', self.gf('django.db.models.fields.IntegerField')()),
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cce.coldchainequipment': {
            'Meta': {'object_name': 'ColdChainEquipment'},
            'capacity_uom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['core.UnitOfMeasurement']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'cce_coldchainequipment_created_by'", 'null': 'True', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'gross_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'cce_coldchainequipment_modified_by'", 'null': 'True', 'blank': 'True'}),
            'net_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'storage_location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['facilities.Warehouse']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cce.ColdChainEquipmentType']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'cce.coldchainequipmenttype': {
            'Meta': {'object_name': 'ColdChainEquipmentType'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'cce_coldchainequipmenttype_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'maximum_temperature': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'minimum_temperature': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'cce_coldchainequipmenttype_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'temperature_uom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_address_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_address_modified_by'", 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True', 'null': 'True'}),
            'subdivision': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True', 'null': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True', 'null': 'True'})
        },
        'core.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['core.Address']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.CompanyCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['core.Contact']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_company_created_by'", 'null': 'True', 'blank': 'True'}),
            'footer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_company_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'null': 'True', 'to': "orm['core.Product']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_companycategory_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_companycategory_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['core.CompanyCategory']", 'related_name': "'core_companycategory_sub_company_categories'", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'comment': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_contact_created_by'", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'irc': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jabber': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'mobile': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_contact_modified_by'", 'null': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'}),
            'sip': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '25'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'})
        },
        'core.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_currency_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_currency_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'symbol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'symbol_position': ('django.db.models.fields.CharField', [], {'default': "'before'", 'max_length': '20'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['core.Address']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.EmployeeCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['core.Contact']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_employee_created_by'", 'null': 'True', 'blank': 'True'}),
            'current_company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'employees'", 'to': "orm['core.Company']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'main_company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Company']", 'related_name': "'core_employee_main_company_employees'", 'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_employee_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'blank': 'True', 'null': 'True', 'to': "orm['auth.User']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.employeecategory': {
            'Meta': {'object_name': 'EmployeeCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_employeecategory_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_employeecategory_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['core.EmployeeCategory']", 'related_name': "'core_employeecategory_sub_employee_categories'", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.modeofadministration': {
            'Meta': {'object_name': 'ModeOfAdministration'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_modeofadministration_created_by'", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_modeofadministration_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'base_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_product_created_by'", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_product_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_productcategory_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_productcategory_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['core.ProductCategory']", 'related_name': "'sub_product_categories'", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.productitem': {
            'Meta': {'object_name': 'ProductItem'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'country_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_productitem_created_by'", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {}),
            'gtin': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Company']"}),
            'mode_of_use': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['core.ModeOfAdministration']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_productitem_modified_by'", 'null': 'True', 'blank': 'True'}),
            'moh_bar_code': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductPresentation']"}),
            'price_currency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['core.Currency']"}),
            'price_per_unit': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '21'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'product_batch_no': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'volume_per_unit': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'product_item_volume_uom'", 'null': 'True', 'blank': 'True'}),
            'weight_per_unit': ('django.db.models.fields.FloatField', [], {'max_length': '21', 'blank': 'True', 'null': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'product_item_weight_uom'", 'null': 'True', 'blank': 'True'})
        },
        'core.productpresentation': {
            'Meta': {'object_name': 'ProductPresentation'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_productpresentation_created_by'", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_productpresentation_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.unitofmeasurement': {
            'Meta': {'object_name': 'UnitOfMeasurement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_unitofmeasurement_created_by'", 'null': 'True', 'blank': 'True'}),
            'factor': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_unitofmeasurement_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'rate': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'rounding_precision': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True', 'null': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uom_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UOMCategory']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.uomcategory': {
            'Meta': {'object_name': 'UOMCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_uomcategory_created_by'", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'core_uomcategory_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['core.UOMCategory']", 'related_name': "'core_uomcategory_sub_uom_categories'", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'facilities.facility': {
            'Meta': {'_ormbases': ['core.Company'], 'object_name': 'Facility'},
            'catchment_population': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Company']", 'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'facility_operators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Company']", 'related_name': "'facility_operators'", 'null': 'True', 'blank': 'True'}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.FacilityType']"}),
            'global_location_no': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'go_down_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'go_live_date': ('django.db.models.fields.DateField', [], {}),
            'has_electricity': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'has_electronic_dar': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'has_electronic_scc': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'blank': 'True', 'null': 'True'}),
            'is_online': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'is_satellite': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Location']", 'null': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['facilities.Facility']", 'related_name': "'child_facilities'", 'null': 'True', 'blank': 'True'}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'facilities_facilitytype_created_by'", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'facilities_facilitytype_modified_by'", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['facilities.FacilityType']", 'related_name': "'sub_facility_types'", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'facilities.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'ambient_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'ambient_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'cold_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'cold_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'facilities_warehouse_created_by'", 'null': 'True', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_refrigerated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'facilities_warehouse_modified_by'", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'inventory.adjustment': {
            'Meta': {'object_name': 'Adjustment'},
            'adjustment_type': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_adjustment_created_by'", 'null': 'True', 'blank': 'True'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_adjustment_modified_by'", 'null': 'True', 'blank': 'True'}),
            'physical_stock_line': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.PhysicalStockCountLine']"}),
            'previous_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'revised_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'inventory.adjustmenttype': {
            'Meta': {'managed': 'False', 'object_name': 'AdjustmentType'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_adjustmenttype_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_adjustmenttype_modified_by'", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'inventory.consumptionrecord': {
            'Meta': {'object_name': 'ConsumptionRecord'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_consumptionrecord_created_by'", 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_consumptionrecord_modified_by'", 'null': 'True', 'blank': 'True'}),
            'performed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'verified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_consumptionrecord_verifier'", 'to': "orm['core.Employee']"})
        },
        'inventory.consumptionrecordline': {
            'Meta': {'object_name': 'ConsumptionRecordLine'},
            'consumption_record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.ConsumptionRecord']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_consumptionrecordline_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_consumptionrecordline_modified_by'", 'null': 'True', 'blank': 'True'}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity_dispensed': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'inventory.incomingshipment': {
            'Meta': {'object_name': 'IncomingShipment'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_incomingshipment_created_by'", 'null': 'True', 'blank': 'True'}),
            'input_warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Warehouse']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_incomingshipment_modified_by'", 'null': 'True', 'blank': 'True'}),
            'other_source': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'others': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stock_entry_type': ('django.db.models.fields.IntegerField', [], {}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'inventory.incomingshipmentline': {
            'Meta': {'object_name': 'IncomingShipmentLine'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_incomingshipmentline_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_incomingshipmentline_modified_by'", 'null': 'True', 'blank': 'True'}),
            'packed_volume': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'packed_volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_incomingshipmentline_packed_volume_uom'", 'to': "orm['core.UnitOfMeasurement']"}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_incomingshipmentline_quantity_uom'", 'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'voucher': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['orders.Voucher']"}),
            'vvm_stage': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_incomingshipmentline_weight_uom'", 'to': "orm['core.UnitOfMeasurement']"})
        },
        'inventory.inventory': {
            'Meta': {'object_name': 'Inventory'},
            'cce': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['cce.ColdChainEquipment']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_inventory_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_inventory_modified_by'", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Warehouse']"})
        },
        'inventory.inventoryline': {
            'Meta': {'object_name': 'InventoryLine'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'adjustments': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['inventory.Adjustment']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_inventoryline_created_by'", 'null': 'True', 'blank': 'True'}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.Inventory']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_inventoryline_modified_by'", 'null': 'True', 'blank': 'True'}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'volume': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'inventory_inventoryline_volume_uom'", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'inventory_inventoryline_weight_uom'", 'null': 'True', 'blank': 'True'})
        },
        'inventory.outgoingshipment': {
            'Meta': {'object_name': 'OutgoingShipment'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_outgoingshipment_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_outgoingshipment_modified_by'", 'null': 'True', 'blank': 'True'}),
            'output_warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Warehouse']"}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'stock_entry_type': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'inventory.outgoingshipmentline': {
            'Meta': {'object_name': 'OutgoingShipmentLine'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_outgoingshipmentline_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_outgoingshipmentline_modified_by'", 'null': 'True', 'blank': 'True'}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity_after': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_before': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_issued': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_outgoingshipmentline_quantity_uom'", 'to': "orm['core.UnitOfMeasurement']"}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'volume': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'inventory_outgoingshipmentline_volume_uom'", 'null': 'True', 'blank': 'True'}),
            'weight_issued': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']", 'related_name': "'inventory_outgoingshipmentline_weight_uom'", 'null': 'True', 'blank': 'True'})
        },
        'inventory.physicalstockcount': {
            'Meta': {'object_name': 'PhysicalStockCount'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_physicalstockcount_created_by'", 'null': 'True', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_physicalstockcount_modified_by'", 'null': 'True', 'blank': 'True'}),
            'performed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'verified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_physicalstockcount_verifier'", 'to': "orm['core.Employee']"})
        },
        'inventory.physicalstockcountline': {
            'Meta': {'object_name': 'PhysicalStockCountLine'},
            'comment': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_physicalstockcountline_created_by'", 'null': 'True', 'blank': 'True'}),
            'inventory_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_physicalstockcountline_modified_by'", 'null': 'True', 'blank': 'True'}),
            'physical_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'physical_stock_count': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.PhysicalStockCount']"}),
            'product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductItem']"}),
            'quantity_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_physicalstockcountline_quantity_uom'", 'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'vvm_stage': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'inventory.stockentry': {
            'Meta': {'managed': 'False', 'object_name': 'StockEntry'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_stockentry_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'inventory_stockentry_modified_by'", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
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
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'orders_purchaseorder_created_by'", 'null': 'True', 'blank': 'True'}),
            'emergency': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expected_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'orders_purchaseorder_modified_by'", 'null': 'True', 'blank': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'purchaser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_purchaseorder_purchaser'", 'to': "orm['facilities.Facility']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_purchaseorder_supplier'", 'to': "orm['facilities.Facility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'orders.salesorder': {
            'Meta': {'object_name': 'SalesOrder'},
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Employee']"}),
            'completed_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'orders_salesorder_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'orders_salesorder_modified_by'", 'null': 'True', 'blank': 'True'}),
            'planned_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_salesorder_recipient'", 'to': "orm['facilities.Facility']"}),
            'sales_order': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['orders.PurchaseOrder']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_salesorder_supplier'", 'to': "orm['facilities.Facility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'orders.voucher': {
            'Meta': {'object_name': 'Voucher'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'orders_voucher_created_by'", 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'orders_voucher_modified_by'", 'null': 'True', 'blank': 'True'}),
            'recipient_representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_voucher_recipient_representative'", 'to': "orm['core.Employee']"}),
            'sales_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.SalesOrder']"}),
            'supplier_representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_voucher_supplier_representative'", 'to': "orm['core.Employee']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        }
    }

    complete_apps = ['inventory']