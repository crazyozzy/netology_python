documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def name_by_doc(doc_num):
    for docs in documents:
        if doc_num == docs['number']:
            return docs['name']

def shelf_by_doc(doc_num):
    for shelfs in directories:
        if doc_num in directories[shelfs]:
            return shelfs
    return 'Документа нет на полках!'

while True:
    command = input('Введите команду (h - help): ')
    if command == 'h':
        print('p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит')
        print('s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится')
        print('l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"')
        print('a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться')
        print('q - выход из программы')
    if command == 'q':
        break
    if command == 'p':
        name = name_by_doc(input('Введите номер документа: '))
        print(f'Имя владельца документа: {name}')
    if command == 's':
        shelf = shelf_by_doc(input('Введите номер документа: '))
        print(f'Документ лежит на полке: {shelf}')