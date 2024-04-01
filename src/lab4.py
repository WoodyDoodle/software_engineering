class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def greet(self):
        return f"Привет, меня зовут {self._name} и мне {self.__age} лет."


person1 = Person("Елизавета", 20)
print(person1._name)
try:
    print(person1.__age)
except AttributeError:
    print('Неовзможно получить доступ к переменной')


print(person1.greet())