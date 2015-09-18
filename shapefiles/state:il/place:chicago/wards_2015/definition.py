from datetime import date

import boundaries

boundaries.register('chicago-wards-2015',  
    file='',
    last_updated=date(2015, 9, 15),
    name='Chicago Wards 2015',
    singular='Chicago Ward 2015',
    domain='Chicago',
    authority='City of Chicago',
    source_url='https://data.cityofchicago.org/api/geospatial/sp34-6z76?method=export&format=Original',
    licence_url='',
    start_date=date(2015,5,1),
    end_date=None,
    notes='',
    name_func=boundaries.attr('WARD'),
    id_func=boundaries.attr('WARD'),
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

