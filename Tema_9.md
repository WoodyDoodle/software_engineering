# Тема 9. ООП: концепции, принципы и примеры реализации.
Отчет по Теме №9 выполнил:
- Крутиков Дмитрий Геннадьевич
- ИНО ЗБ ПОАС-22-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |

## Самостоятельная работа №1
### Задание Садовник и помидоры.<br>Тесты:<br>1) Вызовите справку по садоводству<br>2) Создайте объекты классов TomatoBush и Gardener<br>3) Используя объект класса Gardener, поухаживайте за кустом с помидорами<br>4) Попробуйте собрать урожай, когда томаты еще не дозрели.<br>Продолжайте ухаживать за ними<br>5) Соберите урожай.

```python
class Tomato:
    states = ['отсутствует', 'цветение', 'зеленый', 'красный']

    # Установка начального состояния роста
    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]

    # Перевод томата на следующую стандию созревания
    def grow(self):
        self._state = Tomato.states[(Tomato.states.index(self._state) + 1) % len(Tomato.states)]

    def is_ripe(self):
        return self._state == 'красный'


class TomatoBush:
    # Список всех томатов
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    # Рост томатов на кусте
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверка спелости
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Очищение куста
    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    # Определение свойств имя и растение
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Уход за садом
    def work(self):
        self._plant.grow_all()
        print(f'{self.name} Позаботился(ась) о растении.')

    # Проверка спелости и сбор урожая. Если все спелые, то сбор урожая
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f'Томаты красные. {self.name} собрал(а) урожай.')
            self._plant.give_away_all()
        else:
            print('Томаты ещё не красные')

    # Статический метод, выводит "справку"
    @staticmethod
    def knowledge_base():
        print('Справка по садоводству')


# Вызов справки по садоводству
Gardener.knowledge_base()

# Создание объектов классов TomatoBush и Gardener
tomato_bush = TomatoBush(int(input('Сколько томатов на кусте?: ')))
gardener = Gardener(input('Ваше имя: '), tomato_bush)

while len(tomato_bush.tomatoes) != 0:
    action = int(input('Выберите действие: 1 - позаботиться о саде; 2 - Попробовать собрать урожай: '))
    if action == 1:
        gardener.work()  # Уход за кустом
    elif action == 2:
        gardener.harvest()  # Сбор урожая
        print()
    else:
        print('Ошибка, значение не предполагает действия')
```
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/58bdd703-1227-4d4c-8ae9-c42bfd1aa978)




