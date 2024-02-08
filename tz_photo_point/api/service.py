import requests


def get_currency_rate():
    currency_rate_for_day = requests.get(f'https://www.cbr-xml-daily.ru/daily_json.js').json()
    return currency_rate_for_day['Valute']['USD']['Value']
