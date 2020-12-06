# 1. Написать функцию, которая считывает из файла domains.txt
# названия некоторых интернет доменов и возвращает их в виде списка строк (названия возвращать без точки).

import random
import string


def open_file(file_name):
    """reads text file and returns list of domains """
    file = open(file_name, 'r')
    # lines = file.readlines()
    # rezult = []
    # for line in lines:
    #     rezult.append(line.strip('.\n'))
    # return rezult
    return [line.strip('.\n') for line in file.readlines()]


print(open_file('domains.txt'))


# 2. Написать функцию, которая считывает данные из файла names.txt
# и возвращает список всех фамилий из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии)

def open_file_2(file_name):
    """reads text file and returns list of domains """
    file = open(file_name, 'r')
    return [line.split('\t')[1] for line in file.readlines()]


print(open_file_2('names.txt'))

# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2.
# Строку и число генерировать случайным образом. Буквы могут повторяться.
# Пример: miller.249@sgdyyur.com

def generate_email():
    """loads two files and  generated email"""
    domens = open_file('domains.txt')
    names = open_file_2('names.txt')
    name_index = random.randrange(0, len(names))
    name = names[name_index]
    domen_index = random.randrange(0, len(domens))
    domen = domens[domen_index]
    rand_int_1 = random.randint(100, 999)
    rand_len = random.randint(5, 7)
    letters = [random.choice(string.ascii_letters) for letter in range(rand_len)]
    all_letters = "".join(letters)
    email = name + "." + str(rand_int_1) + "@" + all_letters + "." + domen
    return email


print(generate_email())