from .common import *

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'daphne',
    'drf_spectacular',
] + INSTALLED_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'twitter',
        'USER': 'twitter',
        'PASSWORD': '123@456',
        'HOST': 'db',
        'PORT': '5432',
    }
}

