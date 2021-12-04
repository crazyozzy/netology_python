# Взять из папки formats.json.xml файлы с новостями newsafr.json и newsafr.xml
#
# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
#
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted.
#
# Написать программу для файла в формате json.
import json
from pprint import pprint

words_stat = {}

with open('newsafr.json', encoding='utf8') as f:
    json_data = json.load(f)
    for news in json_data['rss']['channel']['items']:
        news_split = news['description'].split()
        for words in news_split:
            if (words not in words_stat.keys()) and (len(words) > 6):
                words_stat[words] = 1
            if words in words_stat.keys():
                words_stat[words] += 1

words_sorted = sorted(words_stat.items(), key=lambda kv: kv[1], reverse=True)
pprint(words_sorted[0:10])