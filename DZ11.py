import json
import re

# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.


def open_file(filename):
    """open file and read json"""
    with open(filename, "r", encoding='utf-8') as file:
        data_json = json.load(file)
        return data_json


people = open_file("data.json")
print(people)

# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid


def get_name(person):
    """get family name or first name"""
    name = person["name"]
    name_elements = name.split()
    return name_elements[-1]


def sort_by_name(people):
    """sort by family name or first name"""
    return sorted(people, key=get_name)

# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.


def get_end_year(person):
    """get date of death"""
    years = person["years"]
    year_end = years.split(" – ")[1]
    year_end_number = re.findall(r"\d+",year_end)
    if "BC" not in year_end:
        return int(year_end_number[0])
    else:
        return - 1*int(year_end_number[0])


def sort_by_year_end(people):
    """sort by date of death"""
    return sorted(people, key=get_end_year)


for pers in sort_by_year_end(people):
    print(pers)


# 4. Написать функцию сортировки по количеству слов в поле "text"

def count_word(person):
    """count words"""
    text = person["text"]
    words = text.split()
    return len(words)


def sort_by_count_word(people):
    """ sort by count words"""
    return sorted(people, key=count_word)

#проверка сортировки
# people_sorted_by_word_count = sort_by_count_word(people)
# for pers in people_sorted_by_word_count:
#     print(len(pers["text"].split()))