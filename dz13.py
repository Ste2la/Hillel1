# Основа ДЗ - ДЗ №8 https://github.com/30nt/IntroProHillel/blob/main/Homeworks/lesson8.txt

# Суть задания - сoздать класс EmailGenerator

# 1. При инициализации класса передавать два параметра - путь к файлу domains.txt и путь к файлу names.txt
# Пример:
# email_generator = EmailGenerator("domains.txt", "names.txt")

# 2. Атрибуты экземпляра класса: domains и names.
# Получаются с помощью методов get_domains() и get_names(). (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# self.domains = get_domains()
# self.names = get_names()

# 3. При выводе на печать экземпляра класса вывести количество элементов в атрибутах domains и names
# Пример:
# print(email_generator)
# >>>len domains = 8, len names = 34

# 4. Написать метод экземпляра класса generate_email() (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# email = email_generator.generate_email()
# print(email)
# >>>miller.249@sgdyyur.com

import string
import random


class EmailGenerator:

    def __init__(self, domain_path, name_path):
        self._domain_path = domain_path
        self._name_path = name_path

        self.domains = self.get_domains()
        self.names = self.get_names()

    def get_names(self):
        file = open(self._name_path, 'r')
        return [line.split('\t')[1] for line in file.readlines()]

    def get_domains(self):
        file = open(self._domain_path, 'r')
        return [line.strip('.\n') for line in file.readlines()]

    def __repr__(self):
        return f'len domains = {len(self.domains)}, len names = {len(self.names)}'

    def generate_email(self):
        name_index = random.randrange(0, len(self.names))
        name = self.names[name_index]
        domen_index = random.randrange(0, len(self.domains))
        domen = self.domains[domen_index]
        rand_int_1 = random.randint(100, 999)
        rand_len = random.randint(5, 7)
        letters = [random.choice(string.ascii_letters) for letter in range(rand_len)]
        all_letters = "".join(letters)
        email = name + "." + str(rand_int_1) + "@" + all_letters + "." + domen
        return email


email_generator = EmailGenerator("domains.txt", "names.txt")
print(email_generator)
email = email_generator.generate_email()
print(email)

