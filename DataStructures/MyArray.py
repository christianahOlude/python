class MyArray:
    def __init__(self, size):
        self.size = 0
        self.capacity = size
        self.data = []

    def add(self, item):
        if self.size != self.capacity:
            self.data.append(item)
            self.size += 1
        else: return "index  out of bound"


    def remove(self, item):
        if item in self.data:
            self.data.remove(item)
            self.size -= 1


    def length(self):
        return self.capacity

    def sorted(self):
        return sorted(self.data)

    def clear(self):
        self.data = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get(self, index):
        return self.data[index]

    def substring(self, start, end):
        return self.data[start:end]

    def size(self):
        return self.size
