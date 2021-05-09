# ||||||||||||ПОДРОБНЕЕ О ГЕНЕРАТОРАХ СПИСКОВ||||||||
a = [1 for i in range(1000)]
# print(a)


a1 = [i ** 2 for i in range(100)]
# print(a1)


a2 = [int(i) for i in range(10) if i % 2 != 0]
# print(a22)


# a3 = input().split()
# a4 = [int(i) for i in a3]
# print(a4)
# ```````````````````````````````````````


# ```````````````````````````````````````
# ||||||||| Генераторы и итераторы. Функция генератор. Создание генератора при помощи yield |||||||||

# Генератор - это итератор, элементы которого можно итерировать только один раз
# Итератор - объект, который поддерживает функцию next(). Помнит о том, какой элемент будет браться следующим
# Итерируемый объект - объект, который предоставляет возможность поочередно обойти свои элементы.
# Может быть преобразован к итератору

a_ = [1, 2, 3]  # список - это итерируемый объект
b_ = iter(a_)  # так мы превращаем итерируемый объект в итератор
# print(next(b_)) # >>>1
# print(next(b_)) # >>>2
# print(next(b_)) # >>>3

# С помощью выражения-ренератор мы може при высоконагруженных задачах хранить в памяти бесконечное
# число элементов, так как генератор их не держит в памяти, а схватывает на лету
c = (i for i in range(100000000))
for i in c:
    print(i)


# # yield - замораживает генератор на каждой итерации. Следующий старт идет с того момента, где произошла заморозка
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
        yield pr


for i in fact(10):
    print(i, end=' ')
# ```````````````````````````````````````


# ```````````````````````````````````````
# #|||| Алгоритм Евклида |||||||||||
# # Но если хотя бы одно из чисел очень большое, что программа становится неэффективной,
# так как тратит слишком много времени на вычисление
# x, y = map(int, input().split())
# while x != y:
#     if x > y:
#         x = x - y
#     else:
#         y = y - x
# print(x)

# # Поэтому есь такой альтернативный вариант
# a = int(input())
# b = int(input()) # b по умолчанию должен быть меньше a
# # a, b = map(int, input().split()) - а здесь не важно, какая переменная больше какой
# while b > 0:
#   # c = a%b
#   # a = b
#   # b = c
#   # ИЛИ
#   a, b = b, a%b
# print(a)
# ```````````````````````````````````````


# ```````````````````````````````````````
# # || Нахождение всех делителей числа |||

# # Эта программа может быть неэффективной, так как займет много времени на вычисление
# n = int(input())
# i = 1
# while i <= n:
#   if n %i == 0:
#     print(i)
#   i += 1


# # Этот алгоритм эффективнее предыдущего в 2 раза, но все равно не идеален
# n = int(input())
# i = 1
# while i <= n // 2:
#   if n %i == 0:
#     print(i)
#   i += 1
# print(n)


# # Данный алгоритм в 1000 раз эффективнее первого
# n = int(input())
# i = 1
# a = []
# while i*i <= n: # или i <= n**0.5:
#   if n %i == 0:
#     a.append(i)
#     if i !=n // i:
#       a.append(n // i)

#   i += 1
# a.sort()
# print(a)
# ```````````````````````````````````````


# ```````````````````````````````````````
# # |||||||| Факториал ||||||||||||||||||
s = 7
res = 1
for i in range(1, s + 1):
    res *= i
# print(res)

x = 1234
s = 0
while x > 0:
    s += x % 10  # таким образом мы итерируемся из, к примеру, числа 1234 сначала по значению 4 и его в счетчик
    # добавляем, потом 3 и так далее
    x //= 10  # здесь мы задаем шаг итерации, что сначала у нас 1234, потом при след шаге 123 и так до тех пор,
#   пока цифр не останется и цикл не закончится
# print(s)
# ```````````````````````````````````````


# ```````````````````````````````````````
# # |||||||| Метод подсчета |||||||||||||||
# from collections import Counter
# s = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 4, 2]
# print(dict(Counter(s)))

# # Или то же самое более сложным методом подсчета
# s = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 4, 2]
# c = [0] * 6  # 6 потому что здесь цифры от 0 до 5 (всего 6)
# for i in s:
#     c[i] += 1  # то есть тот индекс списка <c>, равный текущиму значению <i> будет
#     # пополняться с 0 до того кол-ва, которое оно встретится в списке <s>
# for i in range(6):
#     print(f'Цифра {i} встречается {c[i]} раз(а)')
# ```````````````````````````````````````