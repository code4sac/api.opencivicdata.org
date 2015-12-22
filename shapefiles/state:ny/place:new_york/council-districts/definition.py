from datetime import date

import boundaries

def nyc_namer(feature):
    return 'new-york-council-district-{0}'.format(str(feature.get('CounDist')))

def ocd_id_func(feature):
    division = 'ocd-division/country:us/state:ny/place:new_york'
    return '{0}/council_district:{1}'.format(division,
                                             feature.get('CounDist'))

boundaries.register('nyc-council-districts',  
    file='',
    last_updated=date(2015, 9, 15),
    name='New York City Council Districts',
    singular='New York City Council District',
    domain='New York City',
    authority='New York City Department of City Planning',
    source_url='https://data.cityofnewyork.us/api/geospatial/yusd-j4xi?method=export&format=Shapefile',
    licence_url='',
    start_date=None,
    end_date=None,
    notes='',
    name_func=nyc_namer,
    id_func=ocd_id_func,
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

