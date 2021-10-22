from fast_bitrix24 import Bitrix
import requests
import datetime

course = 'https://www.cbr-xml-daily.ru/daily_json.js'
webhook = 'https://b24-953w5g.bitrix24.ru/rest/1/rn2qiu1g9q158nwh/'

request = requests.get(course).json()

wallet = {
    'EUR': request['Valute']['EUR']['Value'],
    'USD': request['Valute']['USD']['Value'],
    'KZT': request['Valute']['KZT']['Value'],
    'PLN': request['Valute']['PLN']['Value']
}

print(f'Курс валют на {datetime.datetime.now().date()}')
print(*[f'RUB-{k}: {v}' for k, v in wallet.items()], sep='\n')

b = Bitrix(webhook)

try:
    for i in wallet.keys():
        fields = {
            'ID': i,
            'fields': {"AMOUNT": wallet[i]}
        }
        print(b.call('crm.currency.update', fields))
    print('Курсы валют успешно обновлены!')
except Exception:
    print('Ошибка!')
