
__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
number = int(input("Введите число"))
for i in str(number):
    print(int(i))
while(number):
    print(number%10)
    number = number//10


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
temp = ''
var1 = input("Введите первую переменную\n")
var2 = input("Введите вторую переменную\n")
temp = var1
var1 = var2
var2 = temp
print("var1 =",var1,"var2=",var2)
# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
age = int(input("Сколько вам лет?\n"))
if (age>=18):
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")

