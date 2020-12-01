
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str = "маша"
my_str_2 = "миша"

my_str_3 = my_str + my_str_2
my_itog = []

for symbol in set(my_str_3):
    if my_str_3.count(symbol) == 2:
        my_itog.append(symbol)
print(my_itog)
