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
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0',
    'cookie': 'remixstid=2096619183_185b024cf6e4a11ef7; remixflash=0.0.0; remixscreen_depth=24; remixscreen_orient=1; remixdt=7200; remixgp=e25ccb001e13fff8bb4412d17a39edcf; remixlang=0; remixusid=ZDkyNzhkYmQwNmIyMjQ3YjA2NmEyZDRl; remixab=1; remixff=10; remixsid=140760b71faf322fe860e40eda59bed44b548ed010198762c2d15bd0c905a; remixmdv=JVcnKgPLsog1ayJY; remixaudio_date=28-06-2019; remixaudio_background_play_time_=0; remixaudio_background_play_time_limit=1800; remixaudio_show_alert_today=0; remixseenads=0; remixmdevice=1920/1080/1/!!-!!!!'
}

# Ссылка, с которой будут взяты данные
base_url = input('Введите ссылку: \n')
# print('Изменённая строка:', base_url.replace('https://', 'https://m.'))

# Изменение ссылки на мобильную версию сайта
if re.match('https://vk.com', base_url):
    base_url = base_url.replace('https://', 'https://m.')


def vk_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        div = soup.find_all('div', attrs={'class': 'vv_body'})
        for source in div:
            src = source.find('source', attrs={'type': 'video/mp4'})['src']
            print("\nВаша ссылка на скачивание: \n" + src)
    else:
        print('ERROR')


vk_parse(base_url, headers)
