import os
import datetime
from django.core.exceptions import ImproperlyConfigured
from .settings_local import *

# settings we don't override
#TIME_ZONE = 'America/New_York'
#USE_TZ = True
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ocdapi.urls'

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')),
)
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'boundaries',
    'opencivicdata.core.apps.BaseConfig',
    'opencivicdata.legislative.apps.BaseConfig',
    'imago',
    'pupa',
    'ocdapi',
)
if RAVEN_DSN:
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
    RAVEN_CONFIG = {'dsn': RAVEN_DSN}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'default':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['default'],
            'level': 'ERROR',
            'propagate': True,
        },
        'boundaries': {
             'handlers': ['console'],
             'level': 'INFO',
             'formatter': 'simple'
        },
    }
}

BOUNDARIES_SHAPEFILES_DIR = 'shapefiles'
IMAGO_COUNTRY = 'us'
IMAGO_BOUNDARY_MAPPINGS = {
    'nyc-council-districts': {'key': 'placeholder_id',
                              'prefix': '',
                              'ignore': None,
                             },
    'new-york-municipal': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'chicago-municipal': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'chicago-wards-2015': {'key': 'placeholder_id',
                           'prefix': '',
                           'ignore': None,
                          },
    'chicago-precincts-2015': {'key': 'placeholder_id',
                               'prefix': '',
                               'ignore': None,
                              },
    'st-paul-municipal': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'st-paul-wards': {'key': 'placeholder_id',
                      'prefix': '',
                      'ignore': None,
                     },
    'st-paul-precincts': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'illinois-lower-2011': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'illinois-upper-2011': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'la-metro-committee-districts': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'la-metro-supervisory-districts': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
}