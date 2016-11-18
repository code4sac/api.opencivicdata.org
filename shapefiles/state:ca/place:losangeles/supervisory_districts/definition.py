from datetime import date

import boundaries

def sector_namer(feature):
    return 'la-metro-supervisory-district-{0}'.format(feature.get('DISTRICT'))

def ocd_id_func(feature):
    return 'ocd-division/country:us/state:ca/county:los_angeles/council_district:{0}'.format(feature.get('DISTRICT'))

boundaries.register('la-metro-supervisory-districts',
    file='',
    last_updated=date(2016, 11, 18),
    name='LA Metro Supervisory Districts 2016',
    singular='LA Metro Supervisory District 2016',
    domain='Los Angeles County',
    authority='Los Angeles County Metropolitan Transportation',
    source_url='',
    licence_url='',
    start_date=None,
    end_date=None,
    notes='',
    name_func=sector_namer,
    id_func=ocd_id_func,
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)