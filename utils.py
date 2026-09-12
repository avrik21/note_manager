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
        choice = input("Выберите пункт: ")
        if number_check(choice):
            if 0 > int(choice) or number_points <= int(choice):
                print("Введите корректное число")
                continue
            return int(choice)

def input_number():
    while True:
        input_number = input("Введите номер заметки: ")
        if number_check(input_number):
            return int(input_number)

