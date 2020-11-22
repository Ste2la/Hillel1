#####################
#переменная value, тип - int. если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число
value = int(input())
new_value = value/2 if value < 100 else - value
print(new_value)

#######################
# переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно 1, в противном случае - 0
value = int(input())
new_value = 1 if value < 100 else 0
print(new_value)

######################
#переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно True, в противном случае - False
value = int(input())
new_value = True if value < 100 else False
print(new_value)



######################
# переменная my_str, тип - str. Заменить в my_str все маленькие буквы на большие.
my_str = '12345 QWerty !@#$%'
my_str_new = my_str.upper()
print(f' Замена маленьких букв на большие: {my_str_new}')


#######################
#переменная my_str, тип - str. Заменить в my_str все большие буквы на маленькие.
my_str = '12345 QWerty !@#$%'
my_str_new = my_str.lower()
print(f' Замена больших букв на маленькие: {my_str_new}')


#####################
#переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же. Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.
my_str = input()
my_str_new = my_str*2 if len(my_str) < 5 else my_str
print(my_str_new)

####################
#переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же. Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.
my_str = input()
my_str_new = (my_str+my_str[::-1]) if len(my_str) < 5 else my_str
print(my_str_new)

###################
#переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые являются буквой или цифрой.
my_str = '12345 QWerty !@#$%'
for symbol in my_str:
    if symbol.isdigit() or  symbol.isalpha():
        print(f' буква или цифра: {symbol}')


####################
#переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой.
my_str = '12345 QWerty !@#$%'
for symbol in my_str:
    if not symbol.isdigit() and  not symbol.isalpha():
        print(f' не буква и не число: {symbol}')

####################
#есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой и не пробел.
my_str = '12345 QWerty !@#$%'
for symbol in my_str:
    if not symbol.isdigit() and  not symbol.isalpha() and  not symbol.isspace():
        print(f' не буква, не число, не пробел:  {symbol}' )


