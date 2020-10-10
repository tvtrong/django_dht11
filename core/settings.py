#from pathlib import Path
# coding: utf-8
import os
import re
from decouple import config
from unipath import Path
from dj_database_url import parse as db_url
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = Path(__file__).parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# load production server from .env
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'graphene_django',
    'graphql_playground',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_filters',
    'rest_framework',
    # CORS
    'corsheaders',
    # 'apps.authentication',
    'apps.dht11',
    'apps.home',
    'apps.chats',
]

GRAPHENE = {
    'SCHEMA': 'core.schema.schema',
    'MIDDLEWARE': (
        'graphene_django.debug.DjangoDebugMiddleware',
    )
}

MIDDLEWARE = [
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"   # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(
    BASE_DIR, "core/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

ASGI_APPLICATION = "core.routing.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
            # "hosts": [('127.0.0.1', 6379)],
            'capacity': 1500,
            'expiry': 5,
        },
    },
}


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'DATABASE.sqlite3'),
#    }
# }
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#    'http://localhost:8000',
# )

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'dht11_database',
        'HOST': '127.0.0.1',
        'PORT': 27017,
    }
}

# DATABASES = {
#    'default': config(
#        'DATABASE_URL',
#        default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
#        cast=db_url
#    )
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'vi-vn'

FORMAT_MODULE_PATH = 'core.formats'

TIME_ZONE = 'Asia/Saigon'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'core/static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'VN'

DHT11_GROUP_NAME = 'dht11_latest_data'

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

MESSAGES_TO_LOAD = 15
#EMAIL_HOST = config('EMAIL_HOST', default='localhost')
#EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
#EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
#EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
#EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)

# REST_FRAMEWORK = {
#    'DEFAULT_PERMISSION_CLASSES': [
#        'rest_framework.permissions.IsAuthenticated'
#    ],
#    'DEFAULT_PAGINATION_CLASS':
#        'rest_framework.pagination.LimitOffsetPagination',
#    'PAGE_SIZE': 100
# }
