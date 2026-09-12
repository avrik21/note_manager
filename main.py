import client.ui as ui
import utils as ut

note_ui = ui.NoteUi

while True:
    ut.clear_terminal()
    print("""
    TASK MANAGER
_____________________
1. Добавить заметку;
2. Просмотр заметок;
3. Полный просмотр заметки;
4. Удалить заметку;
5. Сортировать список заметок;
6. Выполнить задачу
0. Выход
_____________________
""")
    choice = ut.input_choice(6)
    if choice == 1:
        ut.function_call(note_ui.request_to_create_note)
    elif choice == 2:
        ut.function_call(note_ui.request_to_show_notes)
    elif choice == 3:
        ut.function_call(note_ui.request_to_view_note)
    elif choice == 4:
        ut.function_call(note_ui.request_to_delete_note)
    elif choice == 5:
        ut.function_call(note_ui.request_to_sort_note)
    elif choice == 6:
        ut.function_call(note_ui.request_to_completed_note)
    elif choice == 0:
        break