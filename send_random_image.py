from pprint import pprint

import requests  # Импортируем библиотеку для работы с запросами

from telegram import Bot
from settings import token

bot = Bot(token=token)
# Адрес API сохраним в константе
URL = 'https://api.imgflip.com/get_memes'
# Сделаем GET-запрос к API
# метод json() преобразует полученный ответ JSON в тип данных, понятный Python
response = requests.get(URL).json()

# Рассмотрим структуру и содержимое переменной response
pprint(response)

# Посмотрим, какого типа переменная response
print(type(response))

# response - это список. А какой длины?
print(len(response))

# Посмотрим, какого типа первый элемент
print(response['data']['memes'][0].get('url'))
