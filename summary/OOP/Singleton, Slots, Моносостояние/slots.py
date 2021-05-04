# Урок 32 Slots в Python
# Using magic method __slots__ we prohibit the class to have more than set attributes
# In this case we lose magic method __dict__ and to thanks this we save member
class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class WithSlots:
    __slots__ = ('x', 'y')  # в __slots__ мы прописываем кортежем атрибуты. Все другие атрибуты будут запрещены

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Объекты __slots__ занимают меньше места в памяти - это преимущество
a = WithoutSlots(3, 4)
b = WithSlots(3, 4)

# так как у объектов без __slots__ все атрибуты хранятся в словаре (__dict__), который тоже занимает место в памяти
# также преимущество в скорости выполнения операций
print(a.__sizeof__(), a.__dict__.__sizeof__())
print(b.__sizeof__())


# _________________________________________________________________________________________________
# Урок 32 Slots свойства Python
# тут с помощью @property мы можем формально обойти запрет от __slots__, так как то, что у нас будет
# под @property - будет свойством, а не атрибутом
class Rectangle:
    __slots__ = '__wight', 'height'

    def __init__(self, z, x):
        self.wight = z  # здесь специально wight не инкапсулируется, чтобы вызывался setter. Потому что тут wight -
        # это уже ссылка на функцию, находящуюся под декоратором @property
        self.height = x

    @property
    def wight(self):
        return self.__wight

    @wight.setter
    def wight(self, value):
        print('setter called')
        self.__wight = value


n = Rectangle(5, 6)
print(n.wight)
print(n._Rectangle__wight)  # получаем доступ к защищеннуму атрибуту, поэтому редактор ругается


# _________________________________________________________________________________________________
# Урок 32 Slots наследование в Python
class Square(Rectangle):
    pass


e = Square(1, 2)

# И тут мы видем весь парадокс ситуации. В экземпляре класса Square уже будет присутствовать переменная __dict__,
# несмотря на то, что в родительском классе это було запрещено из-за __slots__
print(e.__dict__)
e.qwerty = 150
print(e.qwerty)


# Чтобы и в дочернем классе запретить создавать атрибуты, кроме тех, что в __slots__ родительского класса, нам
# нужно заново прописать __slots__. Но тут не нужно прописывать заново атрибуты из кортежа __slots__
class SquareWithSlots(Rectangle):
    __slots__ = ()  # достаточно прописать пустой кортеж

    def __init__(self, w, h):
        super(SquareWithSlots, self).__init__(z=w, x=h)


f = SquareWithSlots(1, 2)
# print(f.__dict__)  # Видим, что не имеем attribute '__dict__'
# Видим, что у нас есть опять атрибуты из __slots__
print(f.wight)
print(f.height)
