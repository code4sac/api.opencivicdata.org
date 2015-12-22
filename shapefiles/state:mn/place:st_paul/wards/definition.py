from datetime import date

import boundaries

def ocd_id_func(feature):
    division = 'ocd-division/country:us/state:mn/place:st_paul'
    ward_number = feature.get('WARD').split('-')[1]
    return '{0}/ward:{1}'.format(division,
                                 ward_number)

def ward_namer(feature):
    ward_number = feature.get('WARD').split('-')[1]
    return 'st-paul-ward-{0}'.format(ward_number)

boundaries.register('st-paul-wards',  
    file='',
    last_updated=date(2015, 9, 15),
    name='Saint Paul Wards',
    singular='Saint Paul Ward',
    domain='Saint Paul',
    authority='City of Saint Paul',
    source_url='https://github.com/datamade/open-divisions/raw/master/ocd-division/country:us/state:mn/place:st_paul/wards/St_Paul_wards.zip',
    licence_url='',
    start_date=date(2015,5,1),
    end_date=None,
    notes='',
    name_func=ward_namer,
    id_func=ocd_id_func,
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

