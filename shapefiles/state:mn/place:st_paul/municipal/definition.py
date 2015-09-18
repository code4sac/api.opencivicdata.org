from datetime import date

import boundaries

boundaries.register('st-paul-municipal',  
    file='',
    last_updated=date(2015, 9, 15),
    name='City of Saint Paul',
    singular='Saint Paul',
    domain='Saint Paul',
    authority='City of Saint Paul',
    source_url='https://github.com/datamade/open-divisions/raw/master/ocd-division/country:us/state:mn/place:st_paul/St_Paul_municipal.zip',
    licence_url='',
    start_date=date(2015,5,1),
    end_date=None,
    notes='',
    name_func=boundaries.attr('NAME'),
    id_func=boundaries.attr('NAME'),
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

