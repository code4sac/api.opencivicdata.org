from datetime import date

import boundaries

def sector_namer(feature):
    print("Running sector_name")
    print(feature.get("Sector"))
    return 'la-metro-committee-district-{0}'.format(feature.get('Sector'))

def ocd_id_func(feature):
    print("Running ocd_id_func")
    print(feature.get("Sector"))
    return 'ocd-division/country:us/state:ca/place:losangeles/district:{0}'.format(feature.get('Sector'))

boundaries.register('la-metro-committee-districts',
    file='',
    last_updated=date(2016, 11, 17),
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


boundaries.register('Federal electoral districts',
    encoding='iso-8859-1',
    last_updated=date(2011, 11, 28),
    name_func=boundaries.clean_attr('FEDENAME'),
)