from datetime import date

import boundaries

boundaries.register('chicago-wards-2003',  
    file='',
    last_updated=date(2015, 4, 16),
    name='Chicago Wards',
    singular='Chicago Ward',
    domain='Chicago',
    authority='City of Chicago',
    source_url='https://data.cityofchicago.org/api/geospatial/xt4z-bnwh?method=export&format=Original',
    licence_url='',
    start_date=date(2003,5,1),
    end_date=date(2015,4,30),
    notes='',
    name_func=boundaries.attr('WARD'),
    id_func=boundaries.attr('WARD'),
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

