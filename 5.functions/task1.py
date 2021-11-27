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
    return 'Документ с таким номером никому не принадлежит!'

def shelf_by_doc(doc_num):
    for shelfs in directories:
        if doc_num in directories[shelfs]:
            return shelfs
    return 'Документа нет на полках!'

def print_documents_list():
    print('type\t\tnumber\t\tname')
    for docs in documents:
        print(f"{docs['type']} \t\"{docs['number']}\"  \t\"{docs['name']}\"")

def add_document():
    doc = {}

    doc['type'] = input('Введите тип документа: ')
    doc['number'] = input('Введите номер документа: ')
    doc['name'] = input('Введите имя владельца: ')
    shelf = input(f'Введите номер полки для документа ({min(directories.keys())}-{max(directories.keys())}): ')
    documents.append(doc)
    add_document_to_shelf(doc['number'], shelf)

def add_document_to_shelf(doc_num, shelf):
    if shelf not in directories.keys():
        print('Такой полки не существует!')
        return 1
    directories[shelf].append(doc_num)
    return 0

def delete_document(doc_to_del):
    del_fact = False
    for docs in documents:
        if docs['number'] == doc_to_del:
            documents.remove(docs)
            del_fact = True
    if del_fact:
        delete_document_from_shelf(doc_to_del)
    else:
        print('Документа не найден!')

def delete_document_from_shelf(doc_to_del):
    shelf = shelf_by_doc(doc_to_del)
    if shelf != 'Документа нет на полках!':
        directories[shelf].remove(doc_to_del)
        return 0
    else:
        print('Указанного документа нет на полках!')
        return 1

def move_document(doc_to_move, new_shelf):
    if new_shelf not in directories.keys():
        print('Целевой полки не существует!')
        return None
    if delete_document_from_shelf(doc_to_move) != 0:
        return 1
    add_document_to_shelf(doc_to_move, new_shelf)

def add_shelf(new_shelf):
    if new_shelf in directories.keys():
        print('Полка с таким номером уже существует!')
        return 2
    directories[new_shelf] = []

def list_shelf(shelf):
    print(directories[shelf])

while True:
    command = input('Введите команду (h - help): ')
    if command == 'h':
        print('p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит')
        print('s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится')
        print('l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"')
        print('a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться')
        print('d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок')
        print('m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую')
        print('as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень')
        print('ls - list shelf - команда, которая спрашивает номер полки и выводит список документов на ней')
        print('q - выход из программы')
    if command == 'q':
        break
    if command == 'p':
        name = name_by_doc(input('Введите номер документа: '))
        print(f'Имя владельца документа: {name}')
    if command == 's':
        shelf = shelf_by_doc(input('Введите номер документа: '))
        print(f'Документ лежит на полке: {shelf}')
    if command == 'l':
        print('Список документов: ')
        print_documents_list()
    if command == 'a':
        add_document()
    if command == 'd':
        delete_document(input('Введите номер документа для удаления: '))
    if command == 'm':
        move_document(input('Введите номер документа для перемещения: '), input(f'Введите целевую полку ({min(directories.keys())}-{max(directories.keys())}): '))
    if command == 'as':
        add_shelf(input('Введите номер новой полки: '))
    if command == 'ls':
        list_shelf(input('Введите номер полки: '))