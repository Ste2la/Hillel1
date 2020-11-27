# 1. Дано целое число (int). Определить сколько нулей в этом числе.
value = 1000003500000
count = str(value).count("0")
print(count)

# # 2. Дано целое число (int). Определить сколько нулей в конце этого числа.

value = 100000020000
value_str = str(value)
count = 0
index = len(value_str)-1
while value_str[index] == "0":
    index -= 1
    count += 1
print(count)


# # # 3. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# # # вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# # # my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 12, 13, 14, 15]
my_list_itog = []

for value in my_list_1:
    if value % 2 == 0:
        my_list_itog.append(value)
for value in my_list_2:
    if value % 2 == 1:
        my_list_itog.append(value)
print(my_list_itog)


# # 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# # стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
#
###
# my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list_2 = my_list_1.copy()
# my_list_2.append(my_list_1[0])
# my_list_2.pop(0)
# print(my_list_2)

###
#my_list_2.append(my_list_2.pop(0))
# print(my_list_2)
###


###
my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_2 = []
my_list_2= my_list_1[1::]
my_list_2.append(my_list_1[0])
print(my_list_2)



# # 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# # [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
#
my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_1.append(my_list_1[0])
my_list_1.pop(0)
print(my_list_1)

# # 6. Дана строка в которой есть числа (разделяются пробелами).
# # Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# # Для данного примера ответ - 133.
#
value = "10 20 30 40"
value2 = value.split()
value3 =[]
for elem in value2:
    value3.append(int(elem))
print(sum(value3))

#
# # 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# # Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# # быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']

my_str = "qwerty0"
itog =[]

for i in range (0,len(my_str),2):
    if i+1 < len(my_str):
        itog.append(my_str[i]+my_str[i+1])
        #print(my_str[i]+my_str[i+1])
    else:
        itog.append(my_str[i]+"_")
        #print(my_str[i]+"_")
print(itog)


# # 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, l_limit,
# # которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# # В переменную sub_str поместить часть строки между этими символами.
# # my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
#
my_str = "abcdef"
l_limit = "a"
r_limit = "f"
my_str2 = []
index = False
for value in my_str:
    if value == r_limit:
        index = False
    if index:
        my_str2.append(value)
    if value == l_limit:
        index = True
print("".join(my_str2))



# # 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# # которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# # В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# # my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "abcdefрпророqwertyf"
l_limit = "a"
r_limit = "f"
my_str2 = []

i = 0
while my_str[i] != l_limit:
    i += 1
j = len(my_str)-1
while my_str[j] != r_limit:
    j -= 1
my_str2 = my_str[i+1:j]

print(my_str2)


# # 10. Дан список чисел. Определите, сколько в этом списке элементов,
# # которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# # Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# # Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

spisok = [1, 9, 2, 8, 3, 7, 4, 6, 5]

count = 0
for i in range (1,len(spisok)-1):
    if spisok[i] > (spisok[i-1] + spisok[i+1]):
        count += 1
print(count)
