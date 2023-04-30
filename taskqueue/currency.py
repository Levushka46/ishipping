import requests

def fetch_currency(currency: str):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    return response.json().get('Valute').get(currency).get('Value')