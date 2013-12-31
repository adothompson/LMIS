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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cce_coldchainequipmenttype_created_by', null=True, blank=True, to=orm['core.Employee'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cce_coldchainequipmenttype_modified_by', null=True, blank=True, to=orm['core.Employee'])),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('minimum_temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('maximum_temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('temperature_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.UnitOfMeasurement'])),
        ))
        db.send_create_signal('cce', ['ColdChainEquipmentType'])

        # Adding model 'ColdChainEquipment'
        db.create_table('cce_coldchainequipment', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cce_coldchainequipment_created_by', null=True, blank=True, to=orm['core.Employee'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cce_coldchainequipment_modified_by', null=True, blank=True, to=orm['core.Employee'])),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=35)),
            ('gross_capacity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('net_capacity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('capacity_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.UnitOfMeasurement'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cce.ColdChainEquipmentType'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'])),
            ('storage_location', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Warehouse'])),
        ))
        db.send_create_signal('cce', ['ColdChainEquipment'])

        # Adding model 'CCETemperatureLog'
        db.create_table('cce_ccetemperaturelog', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cce_ccetemperaturelog_created_by', null=True, blank=True, to=orm['core.Employee'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cce_ccetemperaturelog_modified_by', null=True, blank=True, to=orm['core.Employee'])),
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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cce_cceproblemlog_created_by', null=True, blank=True, to=orm['core.Employee'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cce_cceproblemlog_modified_by', null=True, blank=True, to=orm['core.Employee'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('cce', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cce.ColdChainEquipment'])),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cce.cceproblemlog': {
            'Meta': {'object_name': 'CCEProblemLog'},
            'cce': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cce.ColdChainEquipment']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_cceproblemlog_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_cceproblemlog_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'cce.ccetemperaturelog': {
            'Meta': {'object_name': 'CCETemperatureLog'},
            'cce': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cce.ColdChainEquipment']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_ccetemperaturelog_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'date_time_logged': ('django.db.models.fields.DateTimeField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_ccetemperaturelog_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'temperature': ('django.db.models.fields.FloatField', [], {}),
            'temperature_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'cce.coldchainequipment': {
            'Meta': {'object_name': 'ColdChainEquipment'},
            'capacity_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.UnitOfMeasurement']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_coldchainequipment_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_coldchainequipment_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'storage_location': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Warehouse']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cce.ColdChainEquipmentType']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'cce.coldchainequipmenttype': {
            'Meta': {'object_name': 'ColdChainEquipmentType'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_coldchainequipmenttype_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'maximum_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cce_coldchainequipmenttype_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'temperature_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '35'}),
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '5'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_address_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_address_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'street': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '35'}),
            'subdivision': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '10'}),
            'tag': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'zip': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '15'})
        },
        'core.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Address']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Contact']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_company_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'footer': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'header': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_company_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Product']", 'null': 'True', 'blank': 'True', 'symmetrical': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'comment': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_contact_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'irc': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'jabber': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'mobile': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_contact_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'}),
            'sip': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '25'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'})
        },
        'core.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Address']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.EmployeeCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Contact']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_employee_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'current_company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'employees'", 'to': "orm['core.Company']"}),
            'main_company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_employee_main_company_employees'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Company']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_employee_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'blank': 'True', 'null': 'True', 'to': "orm['auth.User']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.employeecategory': {
            'Meta': {'object_name': 'EmployeeCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_employeecategory_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_employeecategory_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'core_employeecategory_sub_employee_categories'", 'null': 'True', 'blank': 'True', 'to': "orm['core.EmployeeCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.facility': {
            'Meta': {'object_name': 'Facility', '_ormbases': ['core.Company']},
            'catchment_population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Company']", 'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'facility_operators': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'facility_operators'", 'to': "orm['core.Company']", 'null': 'True', 'blank': 'True', 'symmetrical': 'False'}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.FacilityType']"}),
            'global_location_no': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
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
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'child_facilities'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Facility']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'sdp': ('django.db.models.fields.BooleanField', [], {}),
            'supplies_others': ('django.db.models.fields.BooleanField', [], {}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'virtual_facility': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.facilitytype': {
            'Meta': {'object_name': 'FacilityType'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_facilitytype_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_facilitytype_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'sub_facility_types'", 'null': 'True', 'blank': 'True', 'to': "orm['core.FacilityType']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'base_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_product_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_product_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_productcategory_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_productcategory_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'sub_product_categories'", 'null': 'True', 'blank': 'True', 'to': "orm['core.ProductCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.unitofmeasurement': {
            'Meta': {'object_name': 'UnitOfMeasurement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_unitofmeasurement_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_unitofmeasurement_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rounding_precision': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '2'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uom_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UOMCategory']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.uomcategory': {
            'Meta': {'object_name': 'UOMCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_uomcategory_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_uomcategory_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'core_uomcategory_sub_uom_categories'", 'null': 'True', 'blank': 'True', 'to': "orm['core.UOMCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'ambient_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ambient_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'cold_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cold_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_warehouse_created_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'is_refrigerated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_warehouse_modified_by'", 'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'alt_names': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
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
            'code': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['cce']