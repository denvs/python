# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

a = 5
b = 2
print(a, b)
print(a + b)
c = a // b
print(c)
name = input('Введите имя: ')
print('Привет', name)

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

i = int(input('Введите чиисло: '))
print(i, '+ 2 =', i + 2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

i = int(input('Введите ваш возраст: '))
if i >=18 :
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
