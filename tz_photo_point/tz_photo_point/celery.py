import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tz_photo_point.settings')

app = Celery('tz_photo_point')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'create-rate-every-10-second': {
        'task': 'api.tasks.create_new_rate',
        'schedule': 10.0
    }
}
