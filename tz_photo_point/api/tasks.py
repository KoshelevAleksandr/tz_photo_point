from tz_photo_point.celery import app

from .models import Rate
from .service import get_currency_rate


@app.task
def create_new_rate():
    current_rate = get_currency_rate()
    new_rate = Rate.objects.create(currency_rate=current_rate)
    new_rate.save()

