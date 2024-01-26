import requests

from api.models import Rate


def request_currency_rate():
    currency_rate_for_day = requests.get(f'https://www.cbr-xml-daily.ru/daily_json.js').json()
    return currency_rate_for_day['Valute']['USD']['Value']


def create_new_currency_rate():
    current_rate = request_currency_rate()
    Rate.objects.create(currency_rate=current_rate)
