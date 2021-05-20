# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime as dt
import re

"""
Определяется класс "новость" для работы с новостями на сайте РБК.
Конструктору передается ссылка на новость, из которой извлекаются следующие данные,
записываемые в атрибуты класса:
время, дата, заголовок новости, аннотация и текст новости.
(при отсутствии какого-либо параметра в атрибут записывается значение 'N/A')

В классе также имеются метод as_dict(), возвращающий множество атрибутов в виде словаря с 
одноименными ключами, и метод save_to_csv(), обеспечивающий сохранение объекта класса в
'csv' файл с возможностью использования аргументов как в методе to_csv() у pandas.DataFrame.
"""
# Класс "новость".
class News:
    def __init__(self, link):
        news_f = bs(requests.get(link).text, "html.parser")
        date_time = news_f.find(itemprop = "datePublished")
        if date_time:
            self.date, self.time = date_time['content'][:-6].split('T')
        else:
            self.date = 'N/A'
            self.time = 'N/A'
        self.header = news_f.find_all(class_ = "article__header__title")
        if self.header:
            self.header = text_extractor(self.header)
        else:
            self.header = 'N/A'
        self.overview = news_f.find_all(class_ = "article__text__overview")
        if self.overview:
            self.overview = text_extractor(self.overview)
        else:
            self.overview = 'N/A'
        self.text = ''
        article = news_f.find_all(class_ = 'article__text')
        if article:
            self.text = text_extractor(article)
        if self.text == '':
            self.text = 'N/A'
    # Метод для представления объекта класса в виде словаря.
    def as_dict(self):
        return {'Time': self.time, 'Date': self.date, 'Header': self.header, \
                'Overview': self.overview, 'Text': self.text}
    # Метод для сохранения в 'csv' файл.
    def save_to_csv(self, *args, index = False, header = False, mode = 'a', **kwargs):
        df = pd.DataFrame([[self.time, self.date, self.header, self.overview, self.text]])
        df.columns = ['Time', 'Date', 'Header', 'Overview', 'Text']
        df.to_csv(*args, index = index, header = header, mode = mode, **kwargs)

# Функция для извлечения необходимого текстового содержимого из тегов страницы с новостью.
# Подробнее о ее работе см. "readme.txt"
def text_extractor(tags):
    tags_excluded = ['div', 'script', 'span']
    classes_included = ['article__text__pro', 'article__special_container']
    result = ''
    for part in tags:
        inner_tags = part.find_all(recursive = False)
        for tag in inner_tags:
            if (tag.name != 'div' or tag['class'][0] in classes_included):
                for sub_tag in tag.find_all():
                    if sub_tag.name in tags_excluded and not sub_tag.find('p'):
                        sub_tag.replace_with('')
                if (len(tag.get_text(strip = True)) != 0):
                    result += (re.sub(r'\s*[\n\t\r\f\v]\s*', '\n', \
                                      ' '.join([t for t in tag.get_text().strip().split(' ')\
                                                if t])) + '\n')
    return result

# Функция формирования ссылки для запроса GET и наименования файла для сохранения новостей
# с учетом тега и дат начала и конца периода поиска (при формировании ссылки также
# используется параметр смещения 'offset')
def url_filename_composer(tag = 'Роснефть', offset = 0, start_date = None, end_date = None):
    if end_date == None: end_date = dt.datetime.today().strftime('%d.%m.%Y')
    if start_date == None: start_date = (dt.datetime.strptime(end_date, '%d.%m.%Y') - \
                                         dt.timedelta(days=7)).strftime('%d.%m.%Y')
    if dt.datetime.strptime(start_date, '%d.%m.%Y') > \
       dt.datetime.strptime(end_date, '%d.%m.%Y'):
           return 'Incorrect dates'
    else:
        return 'https://www.rbc.ru/v10/search/ajax/?project=rbcnews&dateFrom=' + \
                start_date + '&dateTo=' + end_date + '&offset=' + str(offset) + \
                '&limit=10&query=\"' + tag + '\"', \
                'rbc_' + tag.strip('\"') + '_' + start_date.replace('.', '_') + '-' + \
                end_date.replace('.', '_') + '.csv'
