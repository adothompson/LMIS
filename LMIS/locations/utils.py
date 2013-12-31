# encoding=utf-8

import re
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from .models import Location, LocationType, GeoPoint, GeoPoly

# ./manage.py ogrinspect apps/locations/data/CMR_adm/CMR_adm3.shp LocationGeoPoly --srid=4326 --mapping --multi
# ./manage.py dumpdata locations.location locations.locationgeopoly > nga_adm.json


def load_shp(shp, level):
    # Set Up Mappings and Links to SHP files
    state_mapping = {
        'code': 'StateCode',
        'name': 'StateName',
        'source': 'Source',
        'last_modified_gis': 'Timestamp',
        'global_id_text': 'GlobalID',
        'geom': 'MULTIPOLYGON',
    }
    lga_mapping = {
        'code': 'LGACode',
        'name': 'LGAName',
        'parent_code': 'StateCode',
        'source': 'Source',
        'last_modified_gis': 'Timestamp',
        'global_id_text': 'GlobalID',
        'geom': 'MULTIPOLYGON',
    }
    ward_mapping = {
        'code': 'WardCode',
        'name': 'WardName',
        'parent_code': 'LGACode',
        'source': 'Source',
        'last_modified_gis': 'Timestamp',
        'global_id_text': 'GlobalID',
        'geom': 'MULTIPOLYGON',
    }
    hf_mapping = {
        'parent_code': 'Ward',
        'code': 'POI_NAME',
        'category': 'HEALTH_TYP',
        'name': 'POI_NAME_A',
        'geom': 'POINT',
    }

    if level == 'state':
        import_shp_poly(DataSource(shp), state_mapping)
    elif level == 'lga':
        import_shp_poly(DataSource(shp), lga_mapping)
    elif level == 'ward':
        import_shp_poly(DataSource(shp), ward_mapping)
    elif level == 'hf':
        import_shp_point(DataSource(shp), hf_mapping)

    return True


def import_shp_poly(shp, mapping):
    lm_adm = LayerMapping(GeoPoly, shp, mapping, transform=False, encoding='utf-8')
    lm_adm.save(strict=True, verbose=False)

    return True


def import_shp_point(shp, mapping):
    lm_adm = LayerMapping(GeoPoint, shp, mapping, transform=False, encoding='utf-8')
    lm_adm.save(strict=True, verbose=False)

    return True


def create_locations_from_geo(parent_loc):
    # start with states
    states = GeoPoly.objects.filter(parent_code=None)
    state_type, c = LocationType.objects.get_or_create(name="State", code='state')
    lga_type, c = LocationType.objects.get_or_create(name="Local Government Area", code='lga')
    ward_type, c = LocationType.objects.get_or_create(name="Ward", code='ward')
    for state in states:
        # create state object
        state.uuid = re.sub('[{}]', '', state.global_id_text)
        state_loc = Location.objects.create(uuid=state.uuid, name=state.name, parent=parent_loc, location_type=state_type)
        state.location = state_loc
        state.save()
        print("%s %s %s" % (state_loc.name, parent_loc.name, state_loc.poly.uuid))
        # loop through geopoly objects where parent_code e = state.code
        lgas_in_state = GeoPoly.objects.filter(parent_code=state.code)
        for lga in lgas_in_state:
            # create lga location object
            lga.uuid = re.sub('[{}]', '', lga.global_id_text)
            lga_loc = Location.objects.create(uuid=lga.uuid, name=lga.name, parent=state_loc, location_type=lga_type)
            lga.location = lga_loc
            lga.save()
            print("%s %s %s" % (lga_loc.name, lga_loc.parent.name, lga_loc.poly.uuid))
            # loop through geopoly to find wards
            wards_in_lga = GeoPoly.objects.filter(parent_code=lga.code)
            for ward in wards_in_lga:
                #create ward location object
                ward.uuid = re.sub('[{}]', '', ward.global_id_text)
                ward_loc = Location.objects.create(uuid=ward.uuid, name=ward.name, parent=lga_loc, location_type=ward_type)
                ward.location = ward_loc
                print("%s, %s, %s, %s, %s, %s" % (
                    ward_loc.name, ward_loc.parent.name, ward_loc.parent.parent.name, ward_loc.poly.uuid,
                    ward_loc.poly.code, ward_loc.poly.parent_code))
                ward.save()

    return True


def create_locations_from_pt():
    ward_type = LocationType.objects.get(code="ward")
    for hf in GeoPoint.objects.all():
        hf_type, c = LocationType.objects.get_or_create(name='Health Facility', code='HF', sub_name=hf.category)
        # find parent or assign to state (KN in this example)
        try:
            parent_geo = GeoPoly.objects.get(geom__contains=hf.geom, location__location_type=ward_type)
            parent_loc = parent_geo.location
        except GeoPoly.DoesNotExist as e:
            parent_loc = Location.objects.get(name="Nigeria")
            print("################ %s" % e)

        # create HF Location Object
        hf_loc = Location.objects.create(name=hf.name, location_type=hf_type, parent=parent_loc)
        print("%s, %s, %s, %s, %s" % (hf.name, hf_type.name, hf_type.sub_name, parent_loc.name,
                                      parent_loc.location_type))
        hf.location = hf_loc
        hf.save()

    return True

