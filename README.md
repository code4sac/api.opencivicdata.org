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
# Edit ocdapi/settings.py DATABASES to point to your pupa db
python manage.py migrate
python manage.py runserver
```

What is this?
-------------

This repo is essentially just a Django project for deployment- actual API code is a part of several other projects:

* [boundaries](https://github.com/rhymeswithcycle/represent-boundaries) - backs GIS portion
* [imago](https://github.com/opencivicdata/imago) - people, bills, events, etc.
