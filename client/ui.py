from logic.manager.manager import *
from utils import input_number

note_manager = NoteManager()

class NoteUi:
    def request_to_create_note():

        name = input("Введите название: ")
        category = input("Введите категорию: ")
        discription = input("Введите описание: ")
        
        note_manager.create_note(name, category, discription)
        input("Нажмите Enter ")

    def request_to_show_notes():
        note_manager.show_notes()
        input("Нажмите Enter ")

    def request_to_view_note():
        number = input_number()

        note_manager.view_note(number)
        input("Нажмите Enter ")

    def request_to_delete_note():
        number = input_number()
        result = note_manager.delete_note(number)
        if not result:
            print("Такой заметки нет")
            return False

        print("Заметка удалена!")
        input("Нажмите Enter ")

    def request_to_sort_note():
        result = note_manager.sort_note()
        if not result:
            print("Список пуст")
            return False

        print("Список отсортирован!")
        input("Нажмите Enter ")

    def request_to_completed_note():
        number = input_number()
        result = note_manager.completed_note(number)
        if not result:
            print("Такой заметки нет или она уже выполнена")
            return False
        
        print("Заметка выпалнена! Поздравляю!")
        input("Нажмите Enter ")