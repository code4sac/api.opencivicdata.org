from datetime import date

import boundaries

def precinct_namer(feature):
    return 'ward-{0}-precinct-{1}'.format(str(feature.get('WARD')), 
                                          str(feature.get('PRECINCT')))

def ocd_id_func(feature):
    division = 'ocd-division/country:us/state:il/place:chicago'
    return '{0}/ward:{1}/precinct:{2}'.format(division,
                                              str(feature.get('WARD')), 
                                              str(feature.get('PRECINCT')))

boundaries.register('chicago-precincts-2015',  
    file='',
    last_updated=date(2015, 4, 2),
    name='Chicago Precincts 2015',
    singular='Chicago Precinct 2015',
    domain='Chicago',
    authority='City of Chicago',
    source_url='https://data.cityofchicago.org/api/geospatial/uvpq-qeeq?method=export&format=Original',
    licence_url='',
    start_date=date(2015,5,1),
    end_date=None,
    notes='',
    name_func=precinct_namer,
    id_func=ocd_id_func,
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

