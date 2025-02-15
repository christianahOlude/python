class MyArray:
    def __init__(self, array_size):
        self.size = 0
        self.capacity = array_size
        self.data = []

    def add(self, item):
        if self.size != self.capacity:
            self.data.append(item)
            self.size += 1
        else: return "index  out of bound"
        return item

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

    def size_of(self):
        return self.size


