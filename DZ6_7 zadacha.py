# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str = "афродита"
my_str_2 = "николай"
my_itog = []

# my_set_clean = set()
# my_set_clean_2 = set()
# for symbol in set(my_str):
#     if my_str.count(symbol) == 1:
#         my_set_clean.add(symbol)
# #print(my_set_clean)
# for symbol in set(my_str_2):
#     if my_str_2.count(symbol) == 1:
#         my_set_clean_2.add(symbol)
# #print(my_set_clean_2)
# my_itog = list(my_set_clean.intersection(my_set_clean_2))
# print(my_itog)

list_1 = [symbol for symbol in set(my_str) if my_str.count(symbol) == 1]
list_2 = [symbol for symbol in set(my_str_2) if my_str_2.count(symbol) == 1]
my_itog = list(set(list_1).intersection(set(list_2)))
print(my_itog)