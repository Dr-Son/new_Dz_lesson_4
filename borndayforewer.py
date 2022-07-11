"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def year(question, answer):
    year = input(question)
    while year != answer:
        print("Не верно")
        year = input(question)


year('Ввведите год рождения Пушкина?', '1799')



def day(question, answer):
    day = input(question)
    while day != answer:
        print("Не верно")
        day = input(question)
print('Верно')

day('Ввведите день рождения Пушкина?', '6')

pass

def year_day(question, answer):
    a= input(question)
    while a != answer:
        print("Не верно")
        a = input(question)

year_day('Ввведите год рождения Пушкина?', '1799')
year_day('Ввведите день рождения Пушкина?', '6')

