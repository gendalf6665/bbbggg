import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sim_crm.settings')

app = Celery('sim_crm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()