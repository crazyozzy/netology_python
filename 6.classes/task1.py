# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#
# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# и утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:
#
# кормить
# корову и коз доить
# овец стричь
# собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)

class Poultry:
    name = ''
    sound = ''
    type = ''
    collect_type = ''
    animals_list = []
    weight = 0

    def __init__(self, name, type, sound, weight=0, collect_type=None, animals_list=[]):
        self.name = name
        self.type = type
        self.sound = sound
        self.weight = weight
        self.collect_type = collect_type
        self.animals_list.append(name)

    def set_sound(self, sound):
        self.sound = sound
    def get_sound(self):
        return self.sound
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_type(self, type):
        self.type = type
    def get_type(self):
        return self.type
    def get_collect(self):
        return self.collect_type
    def get_weight(self):
        return self.weight
    def collect(self):
        print(f'Собрали {self.get_collect()} у {self.get_type()} по имени {self.get_name()}, {self.get_sound()}')
    def feed(self):
        print(f'{self.get_type().capitalize()} по имени {self.get_name()} покормлен(а), {self.get_sound()}!')
    def list_all_animals(self):
        print(list(self.animals_list))

goose_gray = Poultry('Серый', "гусь", "га-га-га", "яйца")
goose_white = Poultry("Белый", "гусь", "га-га-га", "яйца")
manka = Poultry("Манька", "корова", "му-му", "молоко")
barashek = Poultry("Барашек", "овца", "беее", "шерсть")
kudriashka = Poultry("Кудряшка", "овца", "беее", "шерсть")
koko = Poultry("Ко-Ко", "курица", "куд-кудах", "яйца")
kukareku = Poultry("Кукареку", "петух", "кукареку")
roga = Poultry("Рога", "коза", "мееее", "молоко")
kopita = Poultry("Копыта", "коза", "мееее", "молоко")
kriakva = Poultry("Кряква", "утка", "кря-кря")

goose_white.feed()
goose_gray.collect()
goose_white.list_all_animals()