from datetime import date

import boundaries

def ocd_id_func(feature):
    division = 'ocd-division/country:us/state:mn/place:st_paul'
    precinct_id = feature.get('Precinct')
    ward, precinct = precinct_id[13], precinct_id[17:]
    return '{0}/ward:{1}/precinct:{2}'.format(division,
                                              ward, 
                                              precinct)

def precinct_namer(feature):
    ward, precinct = feature.get('Precinct')[13], feature.get('Precinct')[17:]
    return 'Ward {0}, Precinct {1}'.format(ward, precinct)

boundaries.register('st-paul-precincts',  
    file='',
    last_updated=date(2015, 9, 15),
    name='Saint Paul Precincts',
    singular='Saint Paul Precinct',
    domain='Saint Paul',
    authority='City of Saint Paul',
    source_url='https://github.com/datamade/open-divisions/raw/master/ocd-division/country:us/state:mn/place:st_paul/precincts/St_Paul_precincts.zip',
    licence_url='',
    start_date=date(2015,5,1),
    end_date=None,
    notes='',
    name_func=precinct_namer,
    id_func=ocd_id_func,
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

