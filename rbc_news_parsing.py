# -*- coding: utf-8 -*-

# Импортируется модуль news и необходимые библиотеки.
import news
import requests
import pandas as pd

# Задаются параметры для поиска.
tag = 'Санкт-Петербург'     # Тег поиска.
start_date = '10.09.2020'   # Дата начала периода поиска.
end_date = '19.09.2020'     # Дата конца периода поиска.
offset = 0                  # Смещение в ссылке для запроса GET (в ответ включаются новости
                            # из массива найденных по остальным параметрам новостей, начиная
                            # с номера равного значению этого параметра (нумерация ведется,
                            # начиная с нуля.))

# Задается список для ссылок на страницы найденных новостей, ссылка для запроса GET и 
# наименование файла для сохранения найденных новостей, соответствующие условиям поиска, 
# и список словарей, полученный в ответ на запрос.
links = []
url, filename = news.url_filename_composer(tag, offset, start_date, end_date)
items = requests.get(url).json()['items']

# Цикл заполнения списка ссылок на страницы с новостями, удовлетворяющими уловиям поиска.
while(items != []):
    for i in range(len(items)):
        if items[i]['fronturl'][:6] != 'https:':
            links.append('https:' + items[i]['fronturl'])
        else:
            links.append(items[i]['fronturl'])
    offset += 10
    url = news.url_filename_composer(tag, offset, start_date, end_date)[0]
    items = requests.get(url).json()['items']

# Формирование списка словарей, соответствующих новостям, ссылки на страницы с которыми
# содержатся в списке links. Каждая ссылка используется для создания объекта класса News,
# который с помощью метода as_dict() преобразуется в словарь. 
# Преобразование списка словарей в объект pandas.DataFrame и сохранение его в 'csv' файл.
if links == []:
    print("Новостей не найдено")
else:
    news_list = [news.News(link).as_dict() for link in links]
    news_df = pd.DataFrame(news_list, columns = ['Date', 'Time', 'Header', 'Overview', 'Text'])
    news_df.to_csv(filename, index = False, encoding = 'utf-8', mode = 'w')
    print('Сбор и сохранение новостей завершены.')