import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calendar_project.settings')

app = Celery('calendar_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-event-every-single-minute': {
        'task': 'events.tasks.mail',
        'schedule': crontab(),
    },
}