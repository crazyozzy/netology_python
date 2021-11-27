queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'тест',
    'Тест 4 4 4',
    'Тест 5 5 5 5'
    ]

dict = {}
one_item = 1 / len(queries)

for list_temp in queries:
    # print(len(list_temp.split()))
    curr_len = len(list_temp.split())
    dict[curr_len] = dict.setdefault(curr_len, 0) + one_item

# print(dict)
for items in dict:
    print(f"Поисковых запросов из {items} слов: {dict.get(items) * 100}%")