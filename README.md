Issues?
-------

Issues with the opencivicdata.org API should be filed at the [api.opencivicdata.org issue tracker](https://sunlight.atlassian.net/browse/OCD/component/10001)

All Open Civic Data issues can be browsed and filed at [the Open Civic Data JIRA instance](https://sunlight.atlassian.net/browse/OCD/).

Usage
-----

Instructions assumes that you already have a database populated with scraped
data.

```
mkvirtualenv ocdapi --python=`which python3`
workon ocdapi
export DATABASE_URL=postgis://my-user:@localhost/my-pupa-database
python manage.py migrate
python manage.py runserver
```

Alternatively, you can add the database connection information to
`ocdapi/settings_local.py`:

```
cp ocdapi/settings_local.py.example ocdapi/settings_local.py
```

Then you'll need to edit `ocdapi/settings_local.py` to contain the so that it
contains the correct connection information

To run the app:

```
workon ocdapi
cd <directory where you cloned the repo>
python manage.py runserver
```

What is this?
-------------

This repo is essentially just a Django project for deployment- actual API code is a part of several other projects:

* [boundaries](https://github.com/rhymeswithcycle/represent-boundaries) - backs GIS portion
* [imago](https://github.com/opencivicdata/imago) - people, bills, events, etc.
