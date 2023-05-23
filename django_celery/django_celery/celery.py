from __future__ import absolute_import,unicode_literals
import os 
from celery import Celery
from django.conf import settings
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery.settings')
app= Celery('django_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings,namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')

app.conf.beat_schedule= {
    'test_func': {
        'task': 'celery_app.tasks.test_func',
        'schedule':2,
    },
}


#celery -A celery_app worker  -l info
#celery -A celery_app beat -l info