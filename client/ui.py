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
        
        if not note_manager.delete_note(number):
            print("Такой заметки нет")
            return False

        note_manager.delete_note(number)
        print("Заметка удалена!")
        input("Нажмите Enter ")

    def request_to_sort_note():
        if not note_manager.sort_note():
            print("Список пуст")
            return False

        note_manager.sort_note
        print("Список отсортирован!")
        input("Нажмите Enter ")

    def request_to_completed_note():
        number = input_number()
        
        if not note_manager.completed_note(number):
            print("Такой заметки нет или она уже выполнена")
            return False
        
        note_manager.completed_note(number)
        print("Заметка выпалнена! Поздравляю!")
        input("Нажмите Enter ")