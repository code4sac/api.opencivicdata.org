from datetime import date

import boundaries

boundaries.register('new-york-municipal',  
    file='',
    last_updated=date(2015, 9, 15),
    name='New York City',
    singular='New York City',
    domain='New York City',
    authority='New York City Department of City Planning',
    source_url='https://data.cityofnewyork.us/api/geospatial/yusd-j4xi?method=export&format=Shapefile',
    licence_url='',
    start_date=None,
    end_date=None,
    notes='',
    name_func=boundaries.attr('NAME'),
    id_func=boundaries.attr('NAME'),
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

