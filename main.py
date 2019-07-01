#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Подключаем необходимые библиотеки
# ================================

# Поиск по строке
import re

# Библиотека для имитации запросов
import requests

# Библиотека для работа с полученными данными
from bs4 import BeautifulSoup as bs

# ================================

# Пишем то, как будут запрашиваться данные
headers = {
   'accept': '*/*',
   'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36',
   'cookie': 'remixmdevice=1920/1080/1/!!-!!!!;'
}

# Ссылка, с которой будут взяты данные
base_url = input('Введите ссылку на видео: \n')
# print('Изменённая строка:', base_url.replace('https://', 'https://m.'))

# Изменение ссылки на мобильную версию сайта
if re.match('https://vk.com', base_url):
   base_url = base_url.replace('https://', 'https://m.')


def vk_parse(base_url, headers):
   session = requests.Session()
   request = session.get(base_url, headers=headers)
   if request.status_code == 200:
      soup = bs(request.content, 'html.parser')
      div = soup.find('div', attrs={'class': 'vv_body'})
      src = div.find('source', attrs={'type': 'video/mp4'})['src']
      print("\nТеперь видео доступно для скачивания: \n" + src)
   else:
      print('ERROR')


vk_parse(base_url, headers)
input('\nНажмите Enter, чтобы закрыть программу')
