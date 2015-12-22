from datetime import date

import boundaries

boundaries.register('chicago-municipal',  
    file='',
    last_updated=date(2015, 9, 15),
    name='City of Chicago',
    singular='Chicago',
    domain='Chicago',
    authority='City of Chicago',
    source_url='https://data.cityofchicago.org/api/geospatial/ewy2-6yfk?method=export&format=Original',
    licence_url='',
    start_date=None,
    end_date=None,
    notes='',
    name_func=lambda feature: 'city-of-chicago',
    id_func=boundaries.attr('OBJECTID'),
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

