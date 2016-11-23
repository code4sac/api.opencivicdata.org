from datetime import date

import boundaries

def format_name(name):
    return name.lower().replace(" ", "_").replace("__", "_")

def sector_namer(feature):
    sector_name = format_name(feature.get('Sector'))
    return 'la-metro-committee-district-{0}'.format(sector_name)

def ocd_id_func(feature):
    sector_name = format_name(feature.get('Sector'))
    print(sector_name)
    return 'ocd-division/country:us/state:ca/county:los_angeles/la_metro_sector:{0}'.format(sector_name)

boundaries.register('la-metro-committee-districts',
    file='',
    last_updated=date(2016, 11, 23),
    name='LA Metro Committee Districts 2016',
    singular='LA Metro Committee District 2016',
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

