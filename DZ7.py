# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
from random import randint
random_list = [randint(1, 100) for i in range(20)]
print(random_list)

# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.
triangle = {}
keys = ("A", "B", "C")
for key in keys:
    triangle[key] = (randint(-10, 10), randint(-10, 10))
print(triangle)


# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***
def my_print(my_str):
    """is used to print a string"""
    print("***" + my_str + '***')


my_print("ll'ldgdgdgdfgd   ffjfjf")


# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
spisok = [{"name": "John", "age": 13},
          {"name": "Misha", "age": 38},
          {"name": "Jack", "age": 13},
          {"name": "Oleg", "age": 13}]

# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена
min_age = 20000
for key_1 in spisok:
    if key_1["age"] < min_age:
        min_age = key_1["age"]

for key_1 in spisok:
    if key_1["age"] == min_age:
        print(key_1["name"])

# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена
max_name_len = 0
for key_1 in spisok:
    if len(key_1["name"]) > max_name_len:
        max_name_len = len(key_1["name"])

for key_1 in spisok:
    if len(key_1["name"]) == max_name_len:
        print(key_1["name"])

# в) Посчитать среднее количество лет всех людей из списка.
age_sum = 0
for key_1 in spisok:
    age_sum += key_1["age"]

print(age_sum/len(spisok))


# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
my_dict_1 = {"name": "John", "age": 13, "weight": 40, "height": 167}
my_dict_2 = {"name": "Misha", "age": 18, "gender": "m"}

print(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
keys_only_1 = set(my_dict_1.keys())-(set(my_dict_2.keys()))
print(keys_only_1)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
my_dict_3 = {}
for key_1 in keys_only_1:
    my_dict_3[key_1] = my_dict_1[key_1]
print(my_dict_3)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_union = {}
keys_only_1 = set(my_dict_1.keys())-(set(my_dict_2.keys()))
for key_1 in keys_only_1:
    my_dict_union[key_1] = my_dict_1[key_1]

keys_only_2 = set(my_dict_2.keys())-(set(my_dict_1.keys()))
for key_2 in keys_only_2:
    my_dict_union[key_2] = my_dict_2[key_2]

keys_both = set(my_dict_1.keys()).intersection(set(my_dict_2.keys()))
for key_1_2 in keys_both:
    my_dict_union[key_1_2] = [my_dict_1[key_1_2], my_dict_2[key_1_2]]

print(my_dict_union)

