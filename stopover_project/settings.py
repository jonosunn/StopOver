import os
import psycopg2
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'exhlfdat&vfum(-34*c2uroi(($ww(yo$9pv98=e6p^gl(-eoj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] # May need to be changed

MAPBOX_ACCESS_KEY = 'pk.eyJ1Ijoic3RvcG92ZXJhZG1pbiIsImEiOiJjanRtcHY3YXozeW10NGJvM3c2dWlxZ2xvIn0.1WlrGXizCLdOrV5TXPTc0A'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# Application definition

INSTALLED_APPS = [
    'map.apps.MapConfig',
    'user.apps.UserConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jquery',
    'paypal.standard.ipn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'stopover_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/map')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'stopover_project.wsgi.application'


# Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8mpuegruaai9f',
        'USER': 'blwdfizxidfgsr',
        'PASSWORD': 'fca09f51620fcdcf1a74fd8e7e32f6cac1de9c495c705505451c669be7b5e46c',
        'HOST': 'ec2-54-221-243-211.compute-1.amazonaws.com',
        'PORT': '5432',
        'TEST': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'd551580ks5f1e1',
            'USER': 'sornyxxhqzklyh',
            'PASSWORD': 'ba8784b5daf0495a80b69f785561eedb4c9a8b1f3c4f489ff76f7cbf03358310',
            'HOST': 'ec2-184-72-238-22.compute-1.amazonaws.com',
            'PORT': '5432',
        },
    }
}

# TEST_RUNNER = 'map.discover_runner.HerokuDiscoverRunner'

# Password validation

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


# PAYPAL settings
PAYPAL_RECEIVER_EMAIL = 'anapatricia_teo-facilitator@yahoo.com.ph'
PAYPAL_TEST = True

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Session Timer
SESSION_EXPIRE_SECONDS = 10*60 # 10 minutes session timer

# Static files (CSS, JavaScript, Images)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files
STATICFILES_DIR = (
    os.path.join(BASE_DIR, 'static'),
)

# Activate Django-Heroku
if 'HEROKU' in os.environ:
    django_heroku.settings(locals())

# Parse values of DATABASE_URL and convert for django readability
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)
# DATABASES['default']['TEST'].update(db_from_env)

# Use sqlite3 database when performing unit tests
import sys
if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
    del DATABASES['default']['OPTIONS']['sslmode']
