# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

people = ['Vasya', 'Petya', 'Alex']
salary = [5000, 50000, 600000]

peo_sale = dict(zip(people, salary))
print(peo_sale)
peo_sale = dict(filter(lambda x: x[1] <= 500000, peo_sale.items()))

with open('salary.txt', 'w+', encoding='utf-8') as file:
    for key, value in peo_sale.items():
        file.write(f'{key} - {value}\n')
    file.seek(0)
    for line in file:
        line_split = line.split(' - ')
        print(f'{str(line_split[0]).upper()} {float(line_split[1]) * .87}')
