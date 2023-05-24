from __future__ import absolute_import,unicode_literals
import os 
from celery import Celery
from django.conf import settings
from datetime import timedelta
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery.settings')
app= Celery('django_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')


app.autodiscover_tasks()

app.conf.beat_schedule={
    'send-mail':{
        'task':'celery_app.tasks.test_func',
        'schedule':crontab(hour=12,minute=59),  

    }
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}'),


