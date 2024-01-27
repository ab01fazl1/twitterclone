from .settings import *

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "daphne",
] + INSTALLED_APPS


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "twitter",
        "USER": "postgres",
        "PASSWORD": "mothertrucker",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
