from ..note.note import Note

class NoteManager:
    def __init__(self):
        self.notes = []
        self.number = 0

    def create_note(self, name, category, discription):
        note = Note(name, category, discription)
        self.number += 1
        note.note_number = self.number
        self.notes.append(note)

    def show_notes(self):
        if len(self.notes) == 0:
            print("Список пуст! Пора что-то добавить!")
            return False
        
        for item in self.notes:
            status = "Не выполнено"
            if item.is_completed:
                status = "Выполнено"
            print(item.is_completed)
            print(f"""
Заметка №{item.note_number}
______________________
Название: {item.name}
Категория: {item.category}
Состояние: {status}
_____________________
""")
        return True

    def view_note(self, number):
        for item in self.notes:
            status = "Не выполнено"
            if item.is_completed:
                status = "Выполнено"
            if item.note_number == number:
                print(f"""
Заметка №{item.note_number}
______________________
Название: {item.name}
Категория: {item.category}
Описание: {item.discription}
Состояние: {status}
_____________________
                """)
                return True
        print("Список пуст! Пора что-то добавить!")
        return False

    def delete_note(self, number):
        for item in self.notes:
            if item.note_number == number:
                self.notes.remove(item)
                return True
        return False

    def sort_note(self):
        lst = []
        new_notes = []

        for item in self.notes:
            lst.append(item.name)
        lst.sort()

        for i in lst:
            for q in self.notes:
                if i == q.name:
                    new_notes.append(q)

        if not len(new_notes):
            return False

        self.notes = new_notes
        return True

    def completed_note(self, number):
        for item in self.notes:
            if item.note_number == number:
                if item.is_completed == True:
                    return False
                item.is_completed = True
                return True
        return False