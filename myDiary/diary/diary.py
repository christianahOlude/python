from tkinter.font import names

from diary.entry import Entry

# diary : Diary = Diary()
#
class Diary:
    def __init__(self):

        self.entries: [Entry] = list()
        self.counter:int = 0
        self.name:str = ''
        self.password:str =''
        self.id: int = self.counter+1
        self.isLocked :bool = False


    def generate_id(self):
        self.counter += 1
        id = self.counter
        return id

    def create_entry(self ,title, content):
        entry = Entry(title,content)
        entry =+ self.id
        self.entries.append(entry)
        return self.id

    def delete_entry(self, id):
        if(id in self.entries):
            self.entries.remove(self.entries[id])

    def update_diary(self, id, title, content):


