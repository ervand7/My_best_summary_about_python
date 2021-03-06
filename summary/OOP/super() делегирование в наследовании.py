# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок №29 Делегирование в Python. Функция super(). Delegating methods in python
# # Функция super() позволяет вызвать в дочернем классе помимо текущей функции
# одноименную функцию родительского класса (другими словами - произвести делегирование).
# Сначала пишем super(), потом через точку пишем название функции из
# родительского класса, которую мы хотим вызвать. Принято вызывать эту функцию
# до исполнения аналогичной в дочернем классе.
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = 50
        self.wight = 100

    def breathe(self):
        print('Человек дышит')


class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name=name, surname=surname)
        # если бы прописали self.age до super(), то 25 перезатерлось бы на 50
        self.age = age

    def breathe(self):
        super().breathe()
        print('Доктор дышит')


p = Person('Ivan', 'Ivanov')
d = Doctor('Семен', 'Семенов', 25)

print(d.name, d.surname, d.age, d.wight)
d.breathe()
