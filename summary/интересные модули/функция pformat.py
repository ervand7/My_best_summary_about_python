# основная статья: https://pyneng.readthedocs.io/ru/latest/book/12_useful_modules/pprint.html#id2
from pprint import pformat

# приводит все типы данных в строку
a = {1: (1, 2, 3)}
b = pformat(a, indent=23, width=1, depth=11)
print(b)
print(type(b))