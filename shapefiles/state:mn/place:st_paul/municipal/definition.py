from datetime import date

import boundaries

def ocd_division(feature):
    division = 'ocd-division/country:us/state:mn/place:st_paul'
    return division

def namer(feature):
    return 'city-of-st-paul'

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
    name_func=namer,
    id_func=ocd_division,
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

