from fast_bitrix24 import Bitrix
import requests
import datetime

# данные для взаимодействия с api сервисов
course = 'https://www.cbr-xml-daily.ru/daily_json.js'
webhook = 'https://b24-953w5g.bitrix24.ru/rest/1/rn2qiu1g9q158nwh/'

# запрос на выгрузку данных по валютам
request = requests.get(course).json()

# извлечение курсов необходимых валют
wallet = {
    'EUR': request['Valute']['EUR']['Value'],
    'USD': request['Valute']['USD']['Value'],
    'KZT': request['Valute']['KZT']['Value'],
    'PLN': request['Valute']['PLN']['Value']
}

# вывод в консоль актуальных курсов валют
print(f'Курс валют на {datetime.datetime.now().date()}')
print(*[f'RUB-{k}: {v}' for k, v in wallet.items()], sep='\n')

# создание объекта класса битрикс24
b = Bitrix(webhook)

# обновление курса валют в системе битрикс 24, с обработкой ошибки в случае ее возникновения
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
