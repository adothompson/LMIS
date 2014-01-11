# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UOMCategory'
        db.create_table('core_uomcategory', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_uomcategory_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_uomcategory_modified_by', blank=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, related_name='core_uomcategory_sub_uom_categories', blank=True, to=orm['core.UOMCategory'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('core', ['UOMCategory'])

        # Adding model 'UnitOfMeasurement'
        db.create_table('core_unitofmeasurement', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_unitofmeasurement_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_unitofmeasurement_modified_by', blank=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('uom_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UOMCategory'])),
            ('rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('factor', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rounding_precision', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['UnitOfMeasurement'])

        # Adding model 'Rate'
        db.create_table('core_rate', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_rate_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_rate_modified_by', blank=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('value', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=21)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Currency'])),
        ))
        db.send_create_signal('core', ['Rate'])

        # Adding model 'Currency'
        db.create_table('core_currency', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_currency_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_currency_modified_by', blank=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=5, unique=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15, unique=True)),
            ('symbol_position', self.gf('django.db.models.fields.CharField')(max_length=20, default='before')),
        ))
        db.send_create_signal('core', ['Currency'])

        # Adding model 'Contact'
        db.create_table('core_contact', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_contact_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_contact_modified_by', blank=True, to=orm['auth.User'])),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('sip', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('irc', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('core', ['Contact'])

        # Adding model 'Address'
        db.create_table('core_address', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_address_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_address_modified_by', blank=True, to=orm['auth.User'])),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('subdivision', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Address'])

        # Adding model 'Company'
        db.create_table('core_company', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_company_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_company_modified_by', blank=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Contact'])),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Address'])),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.CompanyCategory'])),
            ('footer', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Company'])

        # Adding M2M table for field products on 'Company'
        m2m_table_name = db.shorten_name('core_company_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm['core.company'], null=False)),
            ('product', models.ForeignKey(orm['core.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['company_id', 'product_id'])

        # Adding model 'CompanyCategory'
        db.create_table('core_companycategory', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_companycategory_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_companycategory_modified_by', blank=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, related_name='core_companycategory_sub_company_categories', blank=True, to=orm['core.CompanyCategory'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('core', ['CompanyCategory'])

        # Adding model 'EmployeeCategory'
        db.create_table('core_employeecategory', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_employeecategory_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_employeecategory_modified_by', blank=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, related_name='core_employeecategory_sub_employee_categories', blank=True, to=orm['core.EmployeeCategory'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('core', ['EmployeeCategory'])

        # Adding model 'Employee'
        db.create_table('core_employee', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_employee_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_employee_modified_by', blank=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Contact'])),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Address'])),
            ('current_company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='employees', to=orm['core.Company'])),
            ('main_company', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_employee_main_company_employees', blank=True, to=orm['core.Company'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.EmployeeCategory'])),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, blank=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['Employee'])

        # Adding model 'Program'
        db.create_table('core_program', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_program_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_program_modified_by', blank=True, to=orm['auth.User'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('core', ['Program'])

        # Adding M2M table for field partners on 'Program'
        m2m_table_name = db.shorten_name('core_program_partners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('program', models.ForeignKey(orm['core.program'], null=False)),
            ('company', models.ForeignKey(orm['core.company'], null=False))
        ))
        db.create_unique(m2m_table_name, ['program_id', 'company_id'])

        # Adding model 'ProgramProductAllocationInfo'
        db.create_table('core_programproductallocationinfo', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_programproductallocationinfo_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_programproductallocationinfo_modified_by', blank=True, to=orm['auth.User'])),
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
        db.send_create_signal('core', ['ProgramProductAllocationInfo'])

        # Adding model 'ProgramProduct'
        db.create_table('core_programproduct', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_programproduct_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_programproduct_modified_by', blank=True, to=orm['auth.User'])),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Program'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Product'])),
            ('unit_per_target', self.gf('django.db.models.fields.IntegerField')()),
            ('current_price_per_unit', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=21)),
            ('price_currency', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Currency'])),
            ('is_active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('core', ['ProgramProduct'])

        # Adding M2M table for field funding_source on 'ProgramProduct'
        m2m_table_name = db.shorten_name('core_programproduct_funding_source')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('programproduct', models.ForeignKey(orm['core.programproduct'], null=False)),
            ('company', models.ForeignKey(orm['core.company'], null=False))
        ))
        db.create_unique(m2m_table_name, ['programproduct_id', 'company_id'])

        # Adding model 'ProcessingPeriod'
        db.create_table('core_processingperiod', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_processingperiod_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_processingperiod_modified_by', blank=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('core', ['ProcessingPeriod'])

        # Adding model 'ProductCategory'
        db.create_table('core_productcategory', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_productcategory_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_productcategory_modified_by', blank=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, related_name='sub_product_categories', blank=True, to=orm['core.ProductCategory'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('core', ['ProductCategory'])

        # Adding model 'Product'
        db.create_table('core_product', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_product_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_product_modified_by', blank=True, to=orm['auth.User'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductCategory'])),
            ('base_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('core', ['Product'])

        # Adding model 'ProductPresentation'
        db.create_table('core_productpresentation', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_productpresentation_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_productpresentation_modified_by', blank=True, to=orm['auth.User'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('core', ['ProductPresentation'])

        # Adding model 'ModeOfAdministration'
        db.create_table('core_modeofadministration', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_modeofadministration_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_modeofadministration_modified_by', blank=True, to=orm['auth.User'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('core', ['ModeOfAdministration'])

        # Adding model 'ProductItem'
        db.create_table('core_productitem', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_productitem_created_by', blank=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='core_productitem_modified_by', blank=True, to=orm['auth.User'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Product'])),
            ('presentation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductPresentation'])),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Company'])),
            ('product_batch_no', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('moh_bar_code', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('gtin', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('price_per_unit', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=21)),
            ('price_currency', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Currency'])),
            ('expiration_date', self.gf('django.db.models.fields.DateField')()),
            ('country_of_origin', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('mode_of_use', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.ModeOfAdministration'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('weight_per_unit', self.gf('django.db.models.fields.FloatField')(max_length=21, null=True, blank=True)),
            ('weight_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='product_item_weight_uom', blank=True, to=orm['core.UnitOfMeasurement'])),
            ('volume_per_unit', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('volume_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='product_item_volume_uom', blank=True, to=orm['core.UnitOfMeasurement'])),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('core', ['ProductItem'])


    def backwards(self, orm):
        # Deleting model 'UOMCategory'
        db.delete_table('core_uomcategory')

        # Deleting model 'UnitOfMeasurement'
        db.delete_table('core_unitofmeasurement')

        # Deleting model 'Rate'
        db.delete_table('core_rate')

        # Deleting model 'Currency'
        db.delete_table('core_currency')

        # Deleting model 'Contact'
        db.delete_table('core_contact')

        # Deleting model 'Address'
        db.delete_table('core_address')

        # Deleting model 'Company'
        db.delete_table('core_company')

        # Removing M2M table for field products on 'Company'
        db.delete_table(db.shorten_name('core_company_products'))

        # Deleting model 'CompanyCategory'
        db.delete_table('core_companycategory')

        # Deleting model 'EmployeeCategory'
        db.delete_table('core_employeecategory')

        # Deleting model 'Employee'
        db.delete_table('core_employee')

        # Deleting model 'Program'
        db.delete_table('core_program')

        # Removing M2M table for field partners on 'Program'
        db.delete_table(db.shorten_name('core_program_partners'))

        # Deleting model 'ProgramProductAllocationInfo'
        db.delete_table('core_programproductallocationinfo')

        # Deleting model 'ProgramProduct'
        db.delete_table('core_programproduct')

        # Removing M2M table for field funding_source on 'ProgramProduct'
        db.delete_table(db.shorten_name('core_programproduct_funding_source'))

        # Deleting model 'ProcessingPeriod'
        db.delete_table('core_processingperiod')

        # Deleting model 'ProductCategory'
        db.delete_table('core_productcategory')

        # Deleting model 'Product'
        db.delete_table('core_product')

        # Deleting model 'ProductPresentation'
        db.delete_table('core_productpresentation')

        # Deleting model 'ModeOfAdministration'
        db.delete_table('core_modeofadministration')

        # Deleting model 'ProductItem'
        db.delete_table('core_productitem')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
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
            'city': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_address_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_address_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'subdivision': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        'core.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Address']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.CompanyCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Contact']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_company_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'footer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_company_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'symmetrical': 'False', 'blank': 'True', 'to': "orm['core.Product']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_companycategory_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_companycategory_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'related_name': "'core_companycategory_sub_company_categories'", 'blank': 'True', 'to': "orm['core.CompanyCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_contact_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'irc': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_contact_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_currency_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_currency_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '5', 'unique': 'True'}),
            'symbol_position': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'before'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Address']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.EmployeeCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Contact']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_employee_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'current_company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'employees'", 'to': "orm['core.Company']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'main_company': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_employee_main_company_employees'", 'blank': 'True', 'to': "orm['core.Company']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_employee_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.employeecategory': {
            'Meta': {'object_name': 'EmployeeCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_employeecategory_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_employeecategory_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'related_name': "'core_employeecategory_sub_employee_categories'", 'blank': 'True', 'to': "orm['core.EmployeeCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.modeofadministration': {
            'Meta': {'object_name': 'ModeOfAdministration'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_modeofadministration_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_modeofadministration_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.processingperiod': {
            'Meta': {'object_name': 'ProcessingPeriod'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_processingperiod_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_processingperiod_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'base_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_product_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_product_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_productcategory_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_productcategory_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'related_name': "'sub_product_categories'", 'blank': 'True', 'to': "orm['core.ProductCategory']"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_productitem_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {}),
            'gtin': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Company']"}),
            'mode_of_use': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.ModeOfAdministration']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_productitem_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'moh_bar_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductPresentation']"}),
            'price_currency': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Currency']"}),
            'price_per_unit': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '21'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'product_batch_no': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'volume_per_unit': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'product_item_volume_uom'", 'blank': 'True', 'to': "orm['core.UnitOfMeasurement']"}),
            'weight_per_unit': ('django.db.models.fields.FloatField', [], {'max_length': '21', 'null': 'True', 'blank': 'True'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'product_item_weight_uom'", 'blank': 'True', 'to': "orm['core.UnitOfMeasurement']"})
        },
        'core.productpresentation': {
            'Meta': {'object_name': 'ProductPresentation'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_productpresentation_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_productpresentation_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_program_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_program_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Company']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.programproduct': {
            'Meta': {'object_name': 'ProgramProduct'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_programproduct_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'current_price_per_unit': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '21'}),
            'funding_source': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Company']"}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_programproduct_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'price_currency': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Currency']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Program']"}),
            'unit_per_target': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.programproductallocationinfo': {
            'Meta': {'object_name': 'ProgramProductAllocationInfo'},
            'adjustment_value': ('django.db.models.fields.IntegerField', [], {}),
            'buffer_percentage': ('django.db.models.fields.FloatField', [], {}),
            'coverage_rate': ('django.db.models.fields.FloatField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_programproductallocationinfo_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lead_time': ('django.db.models.fields.IntegerField', [], {}),
            'max_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'min_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_programproductallocationinfo_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'push': ('django.db.models.fields.BooleanField', [], {}),
            'supply_interval': ('django.db.models.fields.IntegerField', [], {}),
            'target_population': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'wastage_rate': ('django.db.models.fields.FloatField', [], {}),
            'who_ratio': ('django.db.models.fields.FloatField', [], {})
        },
        'core.rate': {
            'Meta': {'object_name': 'Rate'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_rate_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Currency']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_rate_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '21'})
        },
        'core.unitofmeasurement': {
            'Meta': {'object_name': 'UnitOfMeasurement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_unitofmeasurement_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_unitofmeasurement_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_uomcategory_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_uomcategory_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'related_name': "'core_uomcategory_sub_uom_categories'", 'blank': 'True', 'to': "orm['core.UOMCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.vvmstage': {
            'Meta': {'object_name': 'VVMStage', 'managed': 'False'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_vvmstage_created_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'core_vvmstage_modified_by'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        }
    }

    complete_apps = ['core']