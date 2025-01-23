class MySet:
    def __init__(self):
        self.array = []


    def is_empty(self):
        return len(self.array) == 0

    def add(self, value):
        if value not in self.array:
            self.array.append(value)

    def size(self):
        return len(self.array)

    def remove(self, value):
        if value in self.array:
            self.array.remove(value)




