# . Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.

my_list = ['qw', "er", "ty", "ui"]
my_list_2 = []
for index, value in enumerate(my_list):
    if index % 2:
        my_list_2.append(value)
    else:
        my_list_2.append(value[::-1])
print(my_list_2)



# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
#
my_list = ['qwa', "er", "tyeee", "uiy", "as", "dfuuu", "az"]
my_list_2 = []
for value in my_list:
    if value[0] == "a":
        my_list_2.append(value)
print(my_list_2)


# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ['qwa', "er", "tyeee", "uiy", "as", "dfuuu", "az"]
my_list_2 = []

for value in my_list:
    if "a" in value:
        my_list_2.append(value)
print(my_list_2)


# 4. Дан список my_list в котором могум быть как строки так и целые числа.
# Создать новый список в который поместить только строки из my_list.

my_list = ['qwa', 10, "tyeee", "uiy", 5, "dfuuu", "az"]
my_list_2 = []

for value in my_list:
    if type(value) == str:
        my_list_2.append(value)
print(my_list_2)

# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

my_str = "asdfgasdfg ghghf"
my_list = list(set(my_str))
print(my_list)

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str = "asdfgasdfg ghghf"
my_str_2 = "sjkgjdgjd;gdlgkd"

my_set_1 = set(my_str)
my_set_2 = set(my_str_2)
my_list = my_set_1. intersection(my_set_2)
print(my_list)

# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str = "asdfgasdfg ghghf"
my_str_2 = "sjkgjdgjd;gdlgkd"

my_set_1 = set(my_str)
my_set_2 = set(my_str_2)
my_list = my_set_1. union(my_set_2)
print(my_list)


# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность

Anketa = {
    "familia":  "Inanov",
    "imya": "Petr",
    "vozrast": "15",
    "projivanie": {
        "strana" : "Ukraine",
         "gorod": "Odessa",
         "ulica": "Deribasovskaya"
    },
    "rabota": {
     "nalichie": "da",
        "doljnost": "menedjer"
    }
 }

print(Anketa)

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло

Recept = {
    "korgi": {
        "muka" : 300,
        "moloko" : 200,
        "maslo": 200,
        "yaica": 50
    },
    "krem": {
        "sahar":100,
        "maslo":100,
        "vanil": 5,
        "smetana": 100
    },
    "glazur": {
        "kakao":100,
        "sahar": 100,
        "maslo": 50
    }
}

print(Recept)

