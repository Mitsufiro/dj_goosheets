from django.shortcuts import render
import os
from .models import Currency
from pathlib import Path
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from django.db import connection

BASE_DIR = Path(__file__).resolve().parent.parent
# conn = psycopg2.connect(dbname='django_db', user='django_user',
#                         password='django_password', host='localhost', port=5432)  # подключение к БД

# scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
# client = gspread.authorize(creds)
# sheet = client.open('Копия тестовое').worksheet('Лист1')  # открытие документа на googlesheets


def home(request):
    # Currency(num_of_row=2, id_of_items=2, price = 100, delivery_time = '12313', price_rub = 20000).save()
    currency = Currency.objects.all()
    return render(request, rf'{os.path.join(BASE_DIR)}/sheets/templates/sheets/home.html', {'currency': currency})


def run_updater():
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Копия тестовое').worksheet('Лист1')
    currency = Currency.objects.all()
    Currency.objects.all().delete()
    leg = sheet.get_all_records()
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    value_of_currency = float(data['Valute']['USD']['Value'])  # текущий курс
    for i in leg:
        Currency(num_of_row=i['№'], id_of_items=i['заказ №'], price=i['стоимость,$'], delivery_time=i['срок поставки'],
                 price_rub=float(i['стоимость,$']) * value_of_currency).save()
    # return render(request, rf'{os.path.join(BASE_DIR)}/sheets/templates/sheets/home.html', {'currency': currency})
