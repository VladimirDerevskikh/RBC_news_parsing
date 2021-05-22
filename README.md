������ ������ ������������ ��� ���������� �������� � ����� ��� �� ��������� ���� � ����� ������ � ����� 
������������� ������� � ����������� �� ����������� � 'csv' �����. � ������ ������� � ���������� �������� 
������������ ���� ����������� - �����, ����, ���������, ��������� � �����, ������� ������������� ������� 
����� 'csv' ����� � ���������, � ��� ������ ������������� ����������� ��������. ������ �������� � ���� 
���� �������� ��������� "rbc_news_parsing.py" � ������ "news.py" � ���� ���������� �������� ����, ��� ��� 
�������� � ��������, ����������� ���������� ������ �������. ������� ����� ������ ������ "news.py", � ����� 
���� �������� ���������. ��� ����� ���������� ��������������� � ����� ���� ������. � ��� ������ ���� 
������� ��������� ���������� ���������� ������������, � ������ ���������� ���� ������� ������� ������ � 
��������� ������������ "readme.txt". ����� ������� ���� 'rbc_�����-���������_10_09_2020-19_09_2020.csv', 
���������� ���������� ������ ���������. ��� ����������� � Excel ����� ���������� �������� � ���������� �� 
���������, ��� ��� � ������ ��������� ���������� ������������ � ��������� "koi-8" (��� ����, ����� 
��������� ������������ ������������ �������, ��������, ���� �����), � � Excel ����� ���� ������ ��������� 
� ��� ����������� ����������� ���� ����� ������� ���� � ���������� "koi-8". ������������� ������ �� ����� 
����� ����� � ������� ������ ���� Python:

import pandas as pd

n = 120  
df = pd.read_csv('rbc_�����-���������_10_09_2020-19_09_2020.csv', encoding = 'utf-8')  
  
print(df.iloc[n]['Time'])  
print(df.iloc[n]['Date'])  
print(df.iloc[n]['Header'])  
print(df.iloc[n]['Overview'])  
print(df.iloc[n]['Text'])  

����� � ���� ����� 142 �������, ������� n ����� �������� �� 0 �� 141.

������ �������, ������������ � ����������� ������ �� ����� ��� �� ��������� ���� � �������� ���������� 
������� (������������ ������-��������� � ����� ������, � ������� ���������� �� ��������� �� ���� �������), 
������������� � ������ ������ News, ������� ������������ � ������ "news.py", ��������� ����.

��� ��� ����������, � ������ "news.py" ������������ ����� News. ������ ������ ������ �� ���� ������������ 
����� ���������, ���������� ���������� ���������� ����������� �������� � ��������. ����������� ����� 
������ �������� ������ �� �������� � �������� � � ������� ������������ BeautifulSoup ������� �� 
����������� ���� �������� ������ BeautifulSoup (���������� �������� ���������� � ������� ������ "text" 
������� ������, ����������� ����������� ������� get() �� ���������� "requests", ����������� � ������ �� 
�������� � ��������). ���� ��� �������� ���:

news_f = bs(requests.get(link).text, "html.parser"), ��� 'bs' ��� ����������� ������������ ���������� 
BeautifulSoup, ��������������� � ������ ������ "news.py". ����� � ������� ����������� ������� 
BeautifulSoup ������������ ��������� �������� ������, ��������������� ���� ����������� �������:

date (���� ���������� �������), time (����� ���������� �������), header (��������� �������), 
overview (��������� � �������), text (����� �������).

��� ��������� ����������� date � time ������� ����������� ����� find(), ������� ���������� ��� � ��������� 
itemprop="datePublished". ���� ����� ��� ���������, �� ����� ������� �������� �������� "content" ����� �� 
����, �� ����� �������� ������������� ��������� 6 ��������, �������������� ����� �������� ������ �� 
��������, � ���������� ����� ����������� ������� split() � ������������ 'T' �� ��� ����� - ���� � �����, 
������� � ������������ � �������� ������ "date" � "time". ���� �� ������ ���� �� ���������, �� � �������� 
"date" � "time" ������������ �������� 'N/A'. ����������� ������� ����������� � ��� ������ ��������� - ���� 
��������������� ������ ����������� �� �������� � ��������, �� � ������� ������������ �������� 'N/A'. 
��������, ���� � ������� ��� ���������, �� � ������� "overview" ����� �������� �������� 'N/A'.

���������� ������� "���������", "���������" � "�����" ���������� ������ �����, � ������� ������� "class" 
����� �������� "article__header__title", "article__text__overview" � "article__text" ��������������. ��� 
�� ��������� � ������ "news.py" ���� �������� ��������� ������� text_extractor, ������� �� ���� ��������� 
������ �������� "Tag", ���������� ����������� ���������� ������ find_all() � ���������� ���� ������� 
"news_f" ������ BeautifulSoup, � ��������� �� ���� ��������� ���������� ��������������� ����������. ���� 
����� ������ ��� ���������� � ��������������� ��������� ������������ ��������� "class_" (������������ 
����� ������������, � �� "class", ��� ��� "class" �������� ����������������� ������ � Python), ����� 
�������� ������� "Tag", ���������� ���������, ��������� ��� ����� �������. ���� ����� �������� �� 
���������, �� � ��������������� ������� ������������  �������� 'N/A', � ��� ������������� ���������� 
������ - ������������ ��������� �������� ������� text_extractor(). ����� ����, � ������ ������ ������, 
���� ����� ��������� ������ �������� "Tag" �������� ������ ������, �� � ������� "text" ����� ������������ 
�������� 'N/A'.

������ � ������� text_extractor()

��� ��� ���������� ���� - �� ���� ��� ��������� ������ �������� "Tag" (�� ���� - ��� ���� � 
���������������� ���������� �������� "class"), � ����� ��������� �� ���� ��� ����������� ��������� 
����������. ��� ������� ������� "Tag" �� ����� ������ ������� ���������� ��� ���������������� �������� 
��������, ��� ���� ��������� �������� ���� �� ������ � � ���� ����� ������� ���������� inner_tags 
������������� ��������� ������ find_all(), ����������� � ������� ������� "Tag" �� ������, ������ ����� 
������������ � ���������� recursive = False, ����� ����������� ������ ���������������� ������� ���� (����, 
���������� ����������� ��� ���� ������ ����������������� ���������, ����� ���������� ������ ������� ������ 
�����������). ����� ������������ ������� �� ���� ���������������� ��������. ��� ������� ������ ������� � 
��������� - ����� ����� ������� ������ ����������� ������� ���� � �������, ������� �� ���� �������� � 
����������� ��������� �������. ������ ������ �������� ��� ���� <div>, ����� ���, � ������� ������� "class" 
����� �������� 'article__text__pro' ��� 'article__special_container'. ������� ��� �������� ����� ������� 
������ ����������� ������� �������� �������, ������������� � ���, ����� ��� ���� �� ���� "div" ��� (���� 
��� "div") �������� �������� "class" �������������� � ������ "classes_included". � ����� ������ ������� 
text_extractor() ��� ��������� ������, ���������� �������� �������� "class" � ����� <div> � �������� 
������� (������� ���� �������� � ����������� ��������� �������):

classes_included = ['article__text__pro', 'article__special_container']

��� ��� ����������� ������ ����� �������, �� ��� ������, ���� � ������� ����������� ��������, � ������� 
�������� ����� ���������� � ����� <div> ������� ������ �����������, � ������� ������� 'class' ����� 
�����-���� ��� �������� ������ ���� ����. ������ ������� � ��������� ����� �������, ��� ������ ���������� 
�������� ����� ����� ������� ������ ����������� ������ ���������� ���� � �������� �������. ������ ������ 
�������� ���� � ������������� 'div', 'script' ��� 'span' � ��� ���� �� ���������� ������ ���� ���� <p>. 
��� ��� ������������ ����� ����� �������� � ������ "tags_excluded" � ������ ������� text_extractor(), �� 
��� ������, ���� � ������� ����������� �������� � �������� ���� ������������ ������ � �������� �������, 
����� ��������� ���������� ������ ������������.

��� ���������� ��������� ������ ������ ����� ������� ������ ����������� ����� �������, ������������ 
�������� ���� <div>, ���������� ������� �� ����������� ������ ������ find_all() � ������� ���� ������� 
������ �����������, ���������������� ����� �������. ��� ������� ��������� ��������, ����������� � 
���������� ����� ��������, �������� �������� ����, ��� ��� ������������ ���������� � ������ 
"tags_excluded", �� ��� ���� �� �� �������� ������ ���� ���� <p>. ���� ��� ������� �����������, �� ����� 
�������� ���������� �� ������ ������, ��������� ���� ������ �������������� ����� ������� ������ 
����������� �������� ���� ������ �����. ���� ��� �������� ��� ���

...
        if (tag.name != 'div' or tag['class'][0] in classes_included):  
            for sub_tag in tag.find_all():  
                if sub_tag.name in tags_excluded and not sub_tag.find('p'):  
                    sub_tag.replace_with('')  
...


����� ���� �������� ����, ��� �������������� ��� ������� ������ ����������� (� ��� ����������� �������� 
�������) ����� �����-���� ����� ������ �������� � ���� ��� ���, �� � ���������� result (��� ���� 
���������� ������ ������� � ������ ������� text_extractor()) ������������ ��������� ���������� ����� 
��������������� ����. ��� ��������� ����� ����������� ������������ ����� get_text() ������� "Tag" � 
��������� ����� strip (), � ����� ����, ��� �������� �������� �������� ������ ���� � ������ ����� 
���������� �������� �� ���� ������ '\n' ����������� ��������� ������ split() � join() � ������ � 
�������������� ����������� ��������� (����� sub() ������ "re"). ����� � ����� ������������ ���������� 
����������� ����������� ������ �������� ������ '\n' ��� �������� ����������� ��������� ������ 
(������������� ������ �����, ���������� �� ���� ������� text_extractor()) � ������� ������� print(). ����� 
���������� ���� ���� �������� ��� ������� ���� ������ ������ ����������� ������� text_extractor() 
���������� ���������� result, ���������� �������� ����� �� ��������� ��������������� ������ 
�������� "Tag".

������ ������������ ����� News ����� �������� ��������� ������ 

as_dict - ������ ��� ������������� ���������� ������ � ���� ������� � ������� 'Date', 'Time', 'Header', 
'Overview' � 'Text' � ����������, ����������� �� ��������������� ��������� ����������. ����� ������� 
����������� ��� �������� ������� pandas.DataFame, ������������� ��� ���������� �������� � 'csv' �����.

save_to_csv - ������ ��� ���������� ������� (���������� ������) � 'csv' ����. ���������� ������������ 
����������� ������������ �� ��������� ���������� ������ ������������ ������� pandas.DataFrame � 
����������, ���������� ��������������� ������������ ��������� 'Date', 'Time', 'Header', 'Overview' � 
'Text', � ����������� ����������� ������ pandas.DataFrame.to_csv(). ���������� ����������� ������������� 
��� �� ����������, ��� � � ������ to_csv() � pandas.DataFrame, ��� ���� ��������� ��� ��������� �������� 
�� ���������: header = False, index = False � mode = 'a'. ��� �������� ������, ��� � ���������� ���� ����� 
�������������� � �������� ������������ ��� ����������� ����� ������� � ��� ������������ ���� � ������� 
�������� (������� ��� ������ ������������� ��������� ������� pandas.DataFrame � ������ �������������� � 
������ 'append'), � ����� ��� ���������� ������ ������� ��� ���������� (� �������� ����� ��������� ������� 
����� ����������� ��� ������ �������).

������ ���������� ��� ������ News � ������� text_extractor() ������ "news.py" �������� ������� 
url_filename_composer(). ���, ��������� ��� � ���� ������ � ����� �������, � ������������ � �������� 
���������� ���������� ����� �������� �� ����� ���, ������� ������, � ������� ������� ����� ��������� 
��������������� ������ GET � ������� ����� ���, � ����� ������������ ����� ��� ���������� ��������, 
������� �������� ��� � ������ ������ �������� (��������, 'rbc_�����-���������_10_09_2020-19_09_2020.csv'). 
��� ������� ����� ��������� ���������:

tag (�������� �� ��������� - '��������')    - ���, �� �������� ������ �������.  
offset (�������� �� ��������� - 0)          - �������� (��� ���� �������� ����� ������� ���� ��� ���������  
					      ������ �������� ���������).  
start_date (�������� �� ��������� - None)   - ���� ��� ������ ������� ���� �������� �� ����������, �� �  
					      ���� ������������ �������� �� ������ �������� ���������  
					      end_date.  
end_date (�������� �� ��������� - None)     - ���� ��� ������ ������� ���� �������� �� ����������, �� �  
					      ���� ������������ ������� ����.  


������ �� �������� ���������.

��� ��������� ������ � ��������� ����������� ������ GET, �� ������� ������������ ����� � ������� JSON, 
���������� ������� � ����� ������ "items", �������� ������������� �������� � ���� ������ ��������, 
������ �� ������� ������������� ��������� ������� � �������� ������ �� ��� ������� � �������� ��� 
����� "fronturl". ��� ���������� ������ ������� ������������ ������ ���������� ���� (��� �� ������������ 
������������ ���������� ���� ������� url_filename_composer() �� ������ "news.py"):

https://www.rbc.ru/v10/search/ajax/?project=rbcnews&dateFrom=10.08.2020&dateTo=19.09.2020&offset=0&limit=10&query="��������"

� ���� ������ ������������ ��������� ��������� �������:

dateFrom - ������ ������� ������ ��������.  
dateTo   - ����� ������� ������ ��������.  
offset   - �������� ��� ����� ����� �� ����� �� ��������� �������� ��� ���������� � ����� (����������� 
	   �������� �����������, �� ���� ������� ���� ����� ������� �������).  
limit    - ���������� ���������� ��������, ���������� � ������ (� ���� ��������� ���� �������� ������ 
	   ����� ���������� ������ 10).  
query    - ���, �� �������� �������������� ����� ��������.  



������� � ��������� ������������ ����������� �������������� (���������� "requests" � "pandas" � ���������� 
��� ���� ��������� ������ "news.py"). ����� �������� ��������� ������: 

tag        - ���, �� �������� ������ �������.  
start_date - ������ ������� ������ ��������.  
end_date   - ����� ������� ������ ��������.  

� ����� ������������ ���������� offset, ��������������� ������������ ��������� ������� GET. ������� ��� 
�������� ������ ����, � ����� ����� ������������ ��������� ������ ����� while, � ��� ����� ������� ����. 
����� �������� ������ ������ links, ������� ����� ����������� �������� �� �������� � ���������.

����� ����� � ������� ������� url_filename_composer() �� ������ "news.py" �������� ������ ��� �������� 
������� GET � �����������, ���������������� ��������� ���������� tag, start_date, end_date � offset (��� 
������������ � ���������� url), � ����������� ��� ��������� ������������ �����, � ������� ����� 
����������� ��������� ������� (������������ � ���������� filename). ����� ���������� ������ ���������� � 
������� get() �� ���������� "requests", � � ����������� ������� ������ ���������� ����� json(), ����� 
�������� ������������� ������ � ������� JSON, � � ���� ������� ������� �������� �� ����� 'items' � 
������������ � ���������� items.

����� ��������� ��������� � ����� while. ��� �������� �������� ������� ���������� items �� ������� ������. 
������ ����� �� ������� �������� ������ items ����������� � ������������ � ������ links ������ �� �������, 
������������ � �������� ��� ����� 'fronturl' (����� ����, ����������� ����������� �������� �� ������, ���� 
��������� ����� ����� �������� ���������� �� "https:", ��� ������ ������ - � ���� ������ � ������ 
����������� ������ ����������� "https:"). ����� �������� ���������� offset ������������� �� 10, � ������� 
������� url_filename_composer() �� ������ "news.py" ������� �������� ���������� url ������� ���������� 
(�������� "offset" �������������� ������������� �� 10, � ��������� ��������� �������� �����������), 
���������� �� ������ ������� GET ������ ������������ � ���������� items � �������� ��������� � ������ 
����� while. ����� �������, ������ links ���� �������� ������, ���� �� ������� ����� ��� ������ ��������� 
�������, ��������������� �������� ���� ������ � ������ � ����� ������� ������, ���� ���� ������ 
����������� �������� �� ������� �� ���� ��� ����� �������� ����� while (������� ������ - ������� �� 10 
�������� � ��������� (��� ������������) ���� ����� ��������� �� 1 �� 10 ��������).

����� ����� while, ���� ������ links �� ������, �� ���� � ������� ���������� ������ ��������� ������ 
��������������� �������� ��������. ��� ������ ������ �� ������ links ��������� ������ ������ News � 
����������, ���������������� ����������� ����������� �� ������ �������, ������� � ������� ������ as_dict() 
������������� � �������. ����� ���� ������ �������� ������������� � ������ pandas.DataFrame �� ���������, 
���������������� ����������� �������� (columns = ['Date', 'Time', 'Header', 'Overview', 'Text']), ������� 
� ������� ������ to_csv() ����������� � 'csv' ���� � �������������, ��������������� ���������� ������ 
�������� (���������� filename). �� ���� ��������� ��������� ���� ������.

��� ������� ��� ������� � �������������� Python � ��������� ��������� ������:

Python:    3.7.4  
requests:  2.22.0  
pandas:    0.25.1  