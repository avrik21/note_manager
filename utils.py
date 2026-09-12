import os

def clear_terminal():
    os.system("cls")

def function_call(function):
    clear_terminal()
    function()

def number_check(number):
    try:
        int(number)
        return True
    except ValueError:
        print("Только число")

def input_choice(number_points):
    while True:
        choice = int(input("Выберите пункт: "))
        if 0 > choice > number_points:
            print("Введите корректное число")
            continue
        if number_check(choice):
            return choice

def input_number():
    while True:
        input_number = int(input("Введите номер заметки: "))
        if number_check(input_number):
            return input_number

