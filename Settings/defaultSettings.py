"""
Django settings for billing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.conf import global_settings

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ANONYMOUS_USER_ID=-1

SITE_ID=1

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_jinja',
    'guardian',
    'reversion',
    'taggit',
    'pipeline',
    'social.apps.django_app.default',
    'django.contrib.webdesign',
    'rest_framework',
    ##---
    ##non-external apps
    ##--
    'templateBase',
    'blogEngine',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

TEMPLATE_LOADERS = (
    'django_jinja.loaders.FileSystemLoader',
    'django_jinja.loaders.AppLoader',
)

DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static/'

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)



ROOT_URLCONF = 'Settings.urls'

WSGI_APPLICATION = 'Settings.wsgi.application'


'''
This starts the django pipeline config
'''

PIPELINE_COMPILERS = (
  'pipeline.compilers.sass.SASSCompiler',
)

PIPELINE_CSS = {
    'bootflat': {
        'source_filenames': (
         'bootstrap/css/bootstrap.css',
         #bootflat 
         'bootflat/css/bootflat.css',
         #custom
         'custom.css',
        ),
        'output_filename': 'css/bootflat.min.css',
    },
}
PIPELINE_JS = {
    'bootflat': {
        'source_filenames': (
            #bootstrap
            'bootstrap/js/bootstrap.js',
            #bootflat
            'bootflat/js/icheck.min.js',
            'bootflat/js/jquery.fs.selecter.min.js',
            'bootflat/js/jquery.fs.stepper.min.js',
            '',
        ),
        'output_filename': 'js/all.min.js',
    }
}

'''
This ends the django pipeline config
'''

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR+'/django_cache',
    }
}

##Print all emails to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

if False:
    # make all loggers use the console.
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']
