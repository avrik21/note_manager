class Note:
    number = 0
    
    def __init__(self, name, category, discription):
        self.name = name
        self.category = category
        self.discription = discription
        self.is_completed = False
        self.number += 1
        self.note_number = self.number