import requests
import csv
import dateparser
import json

# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).


def get_quotes(how_many, out_file_name="file.csv"):
    """"""
    quotes = set()
    while len(quotes) < how_many:
        url = "http://api.forismatic.com/api/1.0/"
        params = {"method": "getQuote",
                  "format": "json",
                  "key": 1,
                  "lang": "ru"}
        r = requests.get(url, params=params)
        quote = r.json()
        q = (quote["quoteText"], quote["quoteAuthor"], quote["quoteLink"])
        if quote["quoteAuthor"] != "":
            quotes.add(q)
    result = sorted(list(quotes), key=lambda quotes: quotes[1])
    with open(out_file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(result)


get_quotes(5)

# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая список строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.


def read_authors():

    with open('authors.txt') as f:
        my_lines = f.readlines()
        result = filter(lambda x: "birthday" in x or "death" in x, my_lines)

    return result


author_list = read_authors()

# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)


def form_string(line):
    """"""
    x1 = max(line.find("- "),line.find(" - "))
    x2 = max(line.find("'s birthday"), line.find("'s death"))

    date_str = line[0:x1]
    date = dateparser.parse(date_str)
    date_time = date.strftime("%d/%m/%Y")

    name_str = line[x1+2:x2]

    return {"name": name_str, "date": date_time }


def form_strings(lines):
    return list(map(form_string, lines))


result_2 = form_strings(author_list)


# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.

def save_json():
    with open("result.json", "w") as write_file:
        json.dump(result_2, write_file)


save_json()





