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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_uomcategory_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_uomcategory_modified_by')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, blank=True, to=orm['core.UOMCategory'], related_name='core_uomcategory_sub_uom_categories')),
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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_unitofmeasurement_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_unitofmeasurement_modified_by')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('uom_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UOMCategory'])),
            ('rate', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('factor', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('rounding_precision', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True, max_length=2)),
        ))
        db.send_create_signal('core', ['UnitOfMeasurement'])

        # Adding model 'Rate'
        db.create_table('core_rate', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_rate_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_rate_modified_by')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=21, decimal_places=2)),
            ('date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Currency'])),
        ))
        db.send_create_signal('core', ['Rate'])

        # Adding model 'Currency'
        db.create_table('core_currency', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_currency_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_currency_modified_by')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=5, unique=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15, unique=True)),
            ('symbol_position', self.gf('django.db.models.fields.CharField')(default='before', max_length=20)),
        ))
        db.send_create_signal('core', ['Currency'])

        # Adding model 'Contact'
        db.create_table('core_contact', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_contact_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_contact_modified_by')),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(blank=True, max_length=15)),
            ('email', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75)),
            ('fax', self.gf('django.db.models.fields.CharField')(blank=True, max_length=35)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200)),
            ('skype', self.gf('django.db.models.fields.CharField')(blank=True, max_length=35)),
            ('mobile', self.gf('django.db.models.fields.CharField')(blank=True, max_length=15)),
            ('sip', self.gf('django.db.models.fields.CharField')(blank=True, max_length=25)),
            ('irc', self.gf('django.db.models.fields.CharField')(blank=True, max_length=35)),
            ('jabber', self.gf('django.db.models.fields.CharField')(blank=True, max_length=35)),
            ('comment', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
        ))
        db.send_create_signal('core', ['Contact'])

        # Adding model 'Address'
        db.create_table('core_address', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_address_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_address_modified_by')),
            ('tag', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=35)),
            ('street', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=35)),
            ('zip', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=15)),
            ('city', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=35)),
            ('subdivision', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=10)),
            ('country', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=5)),
        ))
        db.send_create_signal('core', ['Address'])

        # Adding model 'Company'
        db.create_table('core_company', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_company_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_company_modified_by')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['core.Contact'], null=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['core.Address'], null=True)),
            ('header', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('footer', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_companycategory_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_companycategory_modified_by')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, blank=True, to=orm['core.CompanyCategory'], related_name='core_companycategory_sub_company_categories')),
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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_employeecategory_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_employeecategory_modified_by')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, blank=True, to=orm['core.EmployeeCategory'], related_name='core_employeecategory_sub_employee_categories')),
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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_employee_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_employee_modified_by')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['core.Contact'], null=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['core.Address'], null=True)),
            ('current_company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Company'], related_name='employees')),
            ('main_company', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Company'], related_name='core_employee_main_company_employees')),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.EmployeeCategory'])),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(null=True, blank=True, to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('core', ['Employee'])

        # Adding model 'FacilityType'
        db.create_table('core_facilitytype', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_facilitytype_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_facilitytype_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=55)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, blank=True, to=orm['core.FacilityType'], related_name='sub_facility_types')),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('core', ['FacilityType'])

        # Adding model 'FacilityTypeApprovedProduct'
        db.create_table('core_facilitytypeapprovedproduct', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_facilitytypeapprovedproduct_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_facilitytypeapprovedproduct_modified_by')),
            ('facility_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.FacilityType'])),
            ('program_product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProgramProduct'])),
            ('max_months_of_stock', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('core', ['FacilityTypeApprovedProduct'])

        # Adding model 'Facility'
        db.create_table('core_facility', (
            ('company_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['core.Company'], unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=55)),
            ('facility_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.FacilityType'])),
            ('supplies_others', self.gf('django.db.models.fields.BooleanField')()),
            ('sdp', self.gf('django.db.models.fields.BooleanField')()),
            ('global_location_no', self.gf('django.db.models.fields.CharField')(blank=True, max_length=55)),
            ('catchment_population', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('has_electricity', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('is_online', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('has_electronic_scc', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('has_electronic_dar', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(blank=True, default=True, null=True)),
            ('go_live_date', self.gf('django.db.models.fields.DateField')()),
            ('go_down_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('is_satellite', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, blank=True, to=orm['core.Facility'], related_name='child_facilities')),
            ('virtual_facility', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('core', ['Facility'])

        # Adding M2M table for field facility_operators on 'Facility'
        m2m_table_name = db.shorten_name('core_facility_facility_operators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facility', models.ForeignKey(orm['core.facility'], null=False)),
            ('company', models.ForeignKey(orm['core.company'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facility_id', 'company_id'])

        # Adding model 'WarehouseType'
        db.create_table('core_warehousetype', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_warehousetype_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_warehousetype_modified_by')),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
        ))
        db.send_create_signal('core', ['WarehouseType'])

        # Adding model 'Warehouse'
        db.create_table('core_warehouse', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_warehouse_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_warehouse_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'])),
            ('is_refrigerated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cold_storage_gross_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('cold_storage_net_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('ambient_storage_gross_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('ambient_storage_net_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
        ))
        db.send_create_signal('core', ['Warehouse'])

        # Adding model 'Program'
        db.create_table('core_program', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_program_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_program_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=55)),
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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_programproductallocationinfo_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_programproductallocationinfo_modified_by')),
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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_programproduct_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_programproduct_modified_by')),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Program'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Product'])),
            ('unit_per_target', self.gf('django.db.models.fields.IntegerField')()),
            ('current_price_per_unit', self.gf('django.db.models.fields.DecimalField')(max_digits=21, decimal_places=2)),
            ('price_currency', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['core.Currency'], null=True)),
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

        # Adding model 'FacilitySupportedProgram'
        db.create_table('core_facilitysupportedprogram', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_facilitysupportedprogram_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_facilitysupportedprogram_modified_by')),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Program'])),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'])),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
        ))
        db.send_create_signal('core', ['FacilitySupportedProgram'])

        # Adding model 'FacilitySupportedProgramProduct'
        db.create_table('core_facilitysupportedprogramproduct', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_facilitysupportedprogramproduct_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_facilitysupportedprogramproduct_modified_by')),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'])),
            ('program_product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProgramProduct'])),
            ('allocation_info', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.ProgramProductAllocationInfo'], unique=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.OrderGroup'])),
        ))
        db.send_create_signal('core', ['FacilitySupportedProgramProduct'])

        # Adding model 'SupervisoryNode'
        db.create_table('core_supervisorynode', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_supervisorynode_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_supervisorynode_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=55)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, blank=True, to=orm['core.SupervisoryNode'], related_name='parent_supervisory_node')),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Facility'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('core', ['SupervisoryNode'])

        # Adding model 'OrderGroup'
        db.create_table('core_ordergroup', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_ordergroup_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_ordergroup_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=55)),
            ('supervisory_node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.SupervisoryNode'])),
        ))
        db.send_create_signal('core', ['OrderGroup'])

        # Adding M2M table for field member_facilities on 'OrderGroup'
        m2m_table_name = db.shorten_name('core_ordergroup_member_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ordergroup', models.ForeignKey(orm['core.ordergroup'], null=False)),
            ('facility', models.ForeignKey(orm['core.facility'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ordergroup_id', 'facility_id'])

        # Adding model 'ProcessingPeriod'
        db.create_table('core_processingperiod', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_processingperiod_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_processingperiod_modified_by')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('core', ['ProcessingPeriod'])

        # Adding model 'ProductCategory'
        db.create_table('core_productcategory', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_productcategory_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_productcategory_modified_by')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(null=True, blank=True, to=orm['core.ProductCategory'], related_name='sub_product_categories')),
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
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_product_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_product_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductCategory'])),
            ('base_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'])),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('core', ['Product'])

        # Adding model 'ProductPresentation'
        db.create_table('core_productpresentation', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_productpresentation_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_productpresentation_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitOfMeasurement'])),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
        ))
        db.send_create_signal('core', ['ProductPresentation'])

        # Adding model 'ModeOfAdministration'
        db.create_table('core_modeofadministration', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_modeofadministration_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_modeofadministration_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
        ))
        db.send_create_signal('core', ['ModeOfAdministration'])

        # Adding model 'ProductItem'
        db.create_table('core_productitem', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=36)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_productitem_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.Employee'], related_name='core_productitem_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Product'])),
            ('presentation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductPresentation'])),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Company'])),
            ('product_batch_no', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('moh_bar_code', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('gtin', self.gf('django.db.models.fields.CharField')(blank=True, max_length=35)),
            ('price_per_unit', self.gf('django.db.models.fields.DecimalField')(max_digits=21, decimal_places=2)),
            ('price_currency', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['core.Currency'], null=True)),
            ('expiration_date', self.gf('django.db.models.fields.DateField')()),
            ('country_of_origin', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('mode_of_use', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['core.ModeOfAdministration'], null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
            ('weight_per_unit', self.gf('django.db.models.fields.FloatField')(null=True, blank=True, max_length=21)),
            ('weight_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.UnitOfMeasurement'], related_name='product_item_weight_uom')),
            ('volume_per_unit', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('volume_uom', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['core.UnitOfMeasurement'], related_name='product_item_volume_uom')),
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

        # Deleting model 'FacilityType'
        db.delete_table('core_facilitytype')

        # Deleting model 'FacilityTypeApprovedProduct'
        db.delete_table('core_facilitytypeapprovedproduct')

        # Deleting model 'Facility'
        db.delete_table('core_facility')

        # Removing M2M table for field facility_operators on 'Facility'
        db.delete_table(db.shorten_name('core_facility_facility_operators'))

        # Deleting model 'WarehouseType'
        db.delete_table('core_warehousetype')

        # Deleting model 'Warehouse'
        db.delete_table('core_warehouse')

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

        # Deleting model 'FacilitySupportedProgram'
        db.delete_table('core_facilitysupportedprogram')

        # Deleting model 'FacilitySupportedProgramProduct'
        db.delete_table('core_facilitysupportedprogramproduct')

        # Deleting model 'SupervisoryNode'
        db.delete_table('core_supervisorynode')

        # Deleting model 'OrderGroup'
        db.delete_table('core_ordergroup')

        # Removing M2M table for field member_facilities on 'OrderGroup'
        db.delete_table(db.shorten_name('core_ordergroup_member_facilities'))

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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
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
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '35'}),
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '5'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_address_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_address_modified_by'"}),
            'street': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '35'}),
            'subdivision': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '10'}),
            'tag': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'zip': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '15'})
        },
        'core.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['core.Address']", 'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['core.Contact']", 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_company_created_by'"}),
            'footer': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'header': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_company_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['core.Product']", 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_companycategory_created_by'"}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_companycategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.CompanyCategory']", 'related_name': "'core_companycategory_sub_company_categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'comment': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_contact_created_by'"}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'irc': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'jabber': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'mobile': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_contact_modified_by'"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'}),
            'sip': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '25'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'})
        },
        'core.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_currency_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_currency_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '5', 'unique': 'True'}),
            'symbol_position': ('django.db.models.fields.CharField', [], {'default': "'before'", 'max_length': '20'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['core.Address']", 'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.EmployeeCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['core.Contact']", 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_employee_created_by'"}),
            'current_company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Company']", 'related_name': "'employees'"}),
            'main_company': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Company']", 'related_name': "'core_employee_main_company_employees'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_employee_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']", 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.employeecategory': {
            'Meta': {'object_name': 'EmployeeCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_employeecategory_created_by'"}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_employeecategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.EmployeeCategory']", 'related_name': "'core_employeecategory_sub_employee_categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.facility': {
            'Meta': {'_ormbases': ['core.Company'], 'object_name': 'Facility'},
            'catchment_population': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['core.Company']", 'unique': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'facility_operators': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'blank': 'True', 'symmetrical': 'False', 'to': "orm['core.Company']", 'related_name': "'facility_operators'"}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.FacilityType']"}),
            'global_location_no': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'go_down_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'go_live_date': ('django.db.models.fields.DateField', [], {}),
            'has_electricity': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'has_electronic_dar': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'has_electronic_scc': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'default': 'True', 'null': 'True'}),
            'is_online': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'is_satellite': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Facility']", 'related_name': "'child_facilities'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'sdp': ('django.db.models.fields.BooleanField', [], {}),
            'supplies_others': ('django.db.models.fields.BooleanField', [], {}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'virtual_facility': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.facilitysupportedprogram': {
            'Meta': {'object_name': 'FacilitySupportedProgram'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_facilitysupportedprogram_created_by'"}),
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_facilitysupportedprogram_modified_by'"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Program']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.facilitysupportedprogramproduct': {
            'Meta': {'object_name': 'FacilitySupportedProgramProduct'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allocation_info': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.ProgramProductAllocationInfo']", 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_facilitysupportedprogramproduct_created_by'"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_facilitysupportedprogramproduct_modified_by'"}),
            'order_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.OrderGroup']"}),
            'program_product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProgramProduct']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.facilitytype': {
            'Meta': {'object_name': 'FacilityType'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_facilitytype_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_facilitytype_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.FacilityType']", 'related_name': "'sub_facility_types'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.facilitytypeapprovedproduct': {
            'Meta': {'object_name': 'FacilityTypeApprovedProduct'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_facilitytypeapprovedproduct_created_by'"}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.FacilityType']"}),
            'max_months_of_stock': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_facilitytypeapprovedproduct_modified_by'"}),
            'program_product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProgramProduct']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.modeofadministration': {
            'Meta': {'object_name': 'ModeOfAdministration'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_modeofadministration_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_modeofadministration_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.ordergroup': {
            'Meta': {'object_name': 'OrderGroup'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_ordergroup_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'member_facilities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['core.Facility']", 'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_ordergroup_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'supervisory_node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.SupervisoryNode']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.processingperiod': {
            'Meta': {'object_name': 'ProcessingPeriod'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_processingperiod_created_by'"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_processingperiod_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'base_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_product_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_product_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_productcategory_created_by'"}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_productcategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.ProductCategory']", 'related_name': "'sub_product_categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.productitem': {
            'Meta': {'object_name': 'ProductItem'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'country_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_productitem_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {}),
            'gtin': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '35'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Company']"}),
            'mode_of_use': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['core.ModeOfAdministration']", 'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_productitem_modified_by'"}),
            'moh_bar_code': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductPresentation']"}),
            'price_currency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['core.Currency']", 'null': 'True'}),
            'price_per_unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '21', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'product_batch_no': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'volume_per_unit': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'volume_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.UnitOfMeasurement']", 'related_name': "'product_item_volume_uom'"}),
            'weight_per_unit': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True', 'max_length': '21'}),
            'weight_uom': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.UnitOfMeasurement']", 'related_name': "'product_item_weight_uom'"})
        },
        'core.productpresentation': {
            'Meta': {'object_name': 'ProductPresentation'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_productpresentation_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_productpresentation_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.program': {
            'Meta': {'object_name': 'Program'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_program_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_program_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Company']", 'symmetrical': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.programproduct': {
            'Meta': {'object_name': 'ProgramProduct'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_programproduct_created_by'"}),
            'current_price_per_unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '21', 'decimal_places': '2'}),
            'funding_source': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Company']", 'symmetrical': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_programproduct_modified_by'"}),
            'price_currency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['core.Currency']", 'null': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Program']"}),
            'unit_per_target': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.programproductallocationinfo': {
            'Meta': {'object_name': 'ProgramProductAllocationInfo'},
            'adjustment_value': ('django.db.models.fields.IntegerField', [], {}),
            'buffer_percentage': ('django.db.models.fields.FloatField', [], {}),
            'coverage_rate': ('django.db.models.fields.FloatField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_programproductallocationinfo_created_by'"}),
            'lead_time': ('django.db.models.fields.IntegerField', [], {}),
            'max_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'min_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_programproductallocationinfo_modified_by'"}),
            'push': ('django.db.models.fields.BooleanField', [], {}),
            'supply_interval': ('django.db.models.fields.IntegerField', [], {}),
            'target_population': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'wastage_rate': ('django.db.models.fields.FloatField', [], {}),
            'who_ratio': ('django.db.models.fields.FloatField', [], {})
        },
        'core.rate': {
            'Meta': {'object_name': 'Rate'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_rate_created_by'"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Currency']"}),
            'date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_rate_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '21', 'decimal_places': '2'})
        },
        'core.supervisorynode': {
            'Meta': {'object_name': 'SupervisoryNode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_supervisorynode_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '55'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_supervisorynode_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.SupervisoryNode']", 'related_name': "'parent_supervisory_node'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.unitofmeasurement': {
            'Meta': {'object_name': 'UnitOfMeasurement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_unitofmeasurement_created_by'"}),
            'factor': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_unitofmeasurement_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'rate': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'rounding_precision': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '2'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uom_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UOMCategory']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.uomcategory': {
            'Meta': {'object_name': 'UOMCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_uomcategory_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_uomcategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.UOMCategory']", 'related_name': "'core_uomcategory_sub_uom_categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.vvmstage': {
            'Meta': {'managed': 'False', 'object_name': 'VVMStage'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_vvmstage_created_by'"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_vvmstage_modified_by'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'ambient_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'ambient_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'cold_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'cold_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_warehouse_created_by'"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Facility']"}),
            'is_refrigerated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_warehouse_modified_by'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        },
        'core.warehousetype': {
            'Meta': {'object_name': 'WarehouseType'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_warehousetype_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['core.Employee']", 'related_name': "'core_warehousetype_modified_by'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '36'})
        }
    }

    complete_apps = ['core']