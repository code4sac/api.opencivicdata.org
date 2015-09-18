from datetime import date

import boundaries

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
    name_func=boundaries.attr('Precinct'),
    id_func=boundaries.attr('PrecinctID'),
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

