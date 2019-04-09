# Inherit from your regular test settings, here the settings files are arranged like those generated from the django-cookiecutter package
from stopover_project.settings import *

# Get the CI environment variable and die if it isn't set; we don't want to risk running this on a production machine as
# all tables will get dropped
# CI = env.bool('CI', default=False) # note this uses django-environ
# if not CI:
#     raise ValueError('CI environment variable not set to true - avoiding start with this test configuration as a safety precaution')

# Register the heroku CI runner, which wipes tables instead of dropping the whole database
# (Heroku users don't have database drop permission)
TEST_RUNNER = 'map.test_suite_runner.HerokuDiscoverRunner'

# Register the test database as being the same as the default (already set in the settings we inherited from). We've used use a heroku addon to provision a new, clean, database into the CI environment, so this should be OK here but DEFINITELY SHOULD NOT BE USED IN PRODUCTION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd8mpuegruaai9f',
        'USER': 'blwdfizxidfgsr',
        'PASSWORD': 'fca09f51620fcdcf1a74fd8e7e32f6cac1de9c495c705505451c669be7b5e46c',
        'HOST': 'ec2-54-221-243-211.compute-1.amazonaws.com',
        'PORT': '5432',
        'TEST': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'd551580ks5f1e1',
            'USER': 'sornyxxhqzklyh',
            'PASSWORD': 'ba8784b5daf0495a80b69f785561eedb4c9a8b1f3c4f489ff76f7cbf03358310',
            'HOST': 'ec2-184-72-238-22.compute-1.amazonaws.com',
            'PORT': '5432',
        },
    }
} # note this uses django-environ
