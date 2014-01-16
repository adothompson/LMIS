# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Program'
        db.create_table('partners_program', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='partners_program_created_by', null=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='partners_program_modified_by', null=True, to=orm['auth.User'])),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=35)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=55)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('partners', ['Program'])

        # Adding M2M table for field partners on 'Program'
        m2m_table_name = db.shorten_name('partners_program_partners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('program', models.ForeignKey(orm['partners.program'], null=False)),
            ('company', models.ForeignKey(orm['core.company'], null=False))
        ))
        db.create_unique(m2m_table_name, ['program_id', 'company_id'])

        # Adding model 'ProgramProductAllocationInfo'
        db.create_table('partners_programproductallocationinfo', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='partners_programproductallocationinfo_created_by', null=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='partners_programproductallocationinfo_modified_by', null=True, to=orm['auth.User'])),
            ('who_ratio', self.gf('django.db.models.fields.FloatField')()),
            ('coverage_rate', self.gf('django.db.models.fields.FloatField')()),
            ('wastage_rate', self.gf('django.db.models.fields.FloatField')()),
            ('buffer_percentage', self.gf('django.db.models.fields.FloatField')()),
            ('target_population', self.gf('django.db.models.fields.IntegerField')()),
            ('min_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('max_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('push', self.gf('django.db.models.fields.BooleanField')()),
            ('lead_time', self.gf('django.db.models.fields.IntegerField')()),
            ('supply_interval', self.gf('django.db.models.fields.IntegerField')()),
            ('adjustment_value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('partners', ['ProgramProductAllocationInfo'])

        # Adding model 'ProgramProduct'
        db.create_table('partners_programproduct', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='partners_programproduct_created_by', null=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='partners_programproduct_modified_by', null=True, to=orm['auth.User'])),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['partners.Program'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Product'])),
            ('unit_per_target', self.gf('django.db.models.fields.IntegerField')()),
            ('current_price_per_unit', self.gf('django.db.models.fields.DecimalField')(max_digits=21, decimal_places=2)),
            ('price_currency', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, to=orm['core.Currency'])),
            ('is_active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('partners', ['ProgramProduct'])

        # Adding M2M table for field funding_source on 'ProgramProduct'
        m2m_table_name = db.shorten_name('partners_programproduct_funding_source')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('programproduct', models.ForeignKey(orm['partners.programproduct'], null=False)),
            ('company', models.ForeignKey(orm['core.company'], null=False))
        ))
        db.create_unique(m2m_table_name, ['programproduct_id', 'company_id'])


    def backwards(self, orm):
        # Deleting model 'Program'
        db.delete_table('partners_program')

        # Removing M2M table for field partners on 'Program'
        db.delete_table(db.shorten_name('partners_program_partners'))

        # Deleting model 'ProgramProductAllocationInfo'
        db.delete_table('partners_programproductallocationinfo')

        # Deleting model 'ProgramProduct'
        db.delete_table('partners_programproduct')

        # Removing M2M table for field funding_source on 'ProgramProduct'
        db.delete_table(db.shorten_name('partners_programproduct_funding_source'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
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
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_address_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_address_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'street': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'subdivision': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'zip': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'})
        },
        'core.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['core.Address']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.CompanyCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['core.Contact']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_company_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'footer': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'header': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_company_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.Product']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_companycategory_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_companycategory_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'core_companycategory_sub_company_categories'", 'null': 'True', 'to': "orm['core.CompanyCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'comment': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_contact_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'irc': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jabber': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'mobile': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_contact_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_currency_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_currency_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'symbol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'symbol_position': ('django.db.models.fields.CharField', [], {'default': "'before'", 'max_length': '20'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'base_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_product_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_product_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '55'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_productcategory_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_productcategory_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'sub_product_categories'", 'null': 'True', 'to': "orm['core.ProductCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.unitofmeasurement': {
            'Meta': {'object_name': 'UnitOfMeasurement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_unitofmeasurement_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'factor': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_unitofmeasurement_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'rate': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'rounding_precision': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '2'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uom_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UOMCategory']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.uomcategory': {
            'Meta': {'object_name': 'UOMCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_uomcategory_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'core_uomcategory_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'core_uomcategory_sub_uom_categories'", 'null': 'True', 'to': "orm['core.UOMCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'partners.program': {
            'Meta': {'object_name': 'Program'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'partners_program_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'partners_program_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Company']", 'symmetrical': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'partners.programproduct': {
            'Meta': {'object_name': 'ProgramProduct'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'partners_programproduct_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'current_price_per_unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '21', 'decimal_places': '2'}),
            'funding_source': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Company']", 'symmetrical': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'partners_programproduct_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'price_currency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['core.Currency']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.Program']"}),
            'unit_per_target': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'partners.programproductallocationinfo': {
            'Meta': {'object_name': 'ProgramProductAllocationInfo'},
            'adjustment_value': ('django.db.models.fields.IntegerField', [], {}),
            'buffer_percentage': ('django.db.models.fields.FloatField', [], {}),
            'coverage_rate': ('django.db.models.fields.FloatField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'partners_programproductallocationinfo_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lead_time': ('django.db.models.fields.IntegerField', [], {}),
            'max_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'min_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'partners_programproductallocationinfo_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'push': ('django.db.models.fields.BooleanField', [], {}),
            'supply_interval': ('django.db.models.fields.IntegerField', [], {}),
            'target_population': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'wastage_rate': ('django.db.models.fields.FloatField', [], {}),
            'who_ratio': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['partners']