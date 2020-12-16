import random
import string
import json
import csv


# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.


def gen_word():
    """"""
    r = random.random()
    if r < 0.1:
        return str(random.randint(0, 1000000))
    else:
        word = [random.choice(string.ascii_letters.lower()) for letter in range(random.randint(1, 15))]
        lst = [".", ",", "\n"]
        r = random.random()
        if r < 0.7:
            word.append(lst[random.randint(0,2)])
        word_str = "".join(word)
        r = random.random()
        if r < 0.5:
            word_str = word_str.capitalize()
        return word_str


print(gen_word())


def gen_string():
    """"""
    word_list = []
    sum_len_word = 0
    len_string = random.randint(100, 1000)
    print(len_string)
    while sum_len_word < len_string:
        word = gen_word()
        word_list.append(word)
        sum_len_word += len(word)+1

    return " ".join(word_list)


print(gen_string())

# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool


def gen_key():
    """"""
    key = "".join([random.choice(string.ascii_letters.lower()) for letter in range(5)])
    return key


def gen_value():
    """"""
    n = random.random()
    if n < 1/3:
        rand_int = random.randint(-100, 100)
        return rand_int
    if 1/3 <= n < 2/3:
        rand_float = random.random()
        return rand_float
    else:
        rand_bool = random.random() > 0.5
        return rand_bool


def get_dict():
    """"""
    res_dict = {}
    num_keys = random.randint(5, 20)
    while len(res_dict) < num_keys:
        res_dict[gen_key()] = gen_value()
    return res_dict


get_dict()
print(get_dict())


# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.


def get_list():
    """"""
    row_count = random.randint(3, 10)
    col_count = random.randint(3, 10)
    rez_list =[]
    for _ in range(row_count):
        rez_list.append([random.randint(0,1) for _ in range(col_count)])
    return rez_list


# Написать функцию generate_and_write_file которая принимает один параметр - имя файла(вместе с путем).
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"


def generate_and_write_file(filename: str):
    """"""

    if filename.lower().endswith('.txt'):
        with open(filename, "w") as file:
            file.write(gen_string())
    elif filename.lower().endswith('.csv'):
        result = get_list()
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(result)
    elif filename.lower().endswith('.json'):
        with open(filename, "w") as write_file:
            json.dump(get_dict(), write_file)
    else:
        print('Unsupported file format')


generate_and_write_file("my_new_file.txt")
generate_and_write_file("my_new_file.json")
generate_and_write_file("my_new_file.csv")
generate_and_write_file("my_new_file.exe")