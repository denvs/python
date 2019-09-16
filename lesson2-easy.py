# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['яблоко', 'банан', 'киви', 'арбуз']

max_len = 0

for fruit in fruits:
    cur_len = len(fruit)
    if cur_len > max_len:
        max_len = cur_len

for fruit in fruits:
    print('{0}.{1:>{2}}'.format(fruits.index(fruit) + 1, fruit, max_len + 1))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_a = [1, 2, 3]
list_b = [3, 4, 5]

for b in list_b:
    if b in list_a:
        list_a.remove(b)
print(list_a)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list = [1, 2, 3, 34, 94, 4, 45]
list_new = []

for el in list:
    if (el % 2) == 0:
        list_new.append(el / 4)
    else:
        list_new.append(el * 2)
print(list_new)