import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twitter.settings.settings-dev')

celery = Celery('twitter')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()