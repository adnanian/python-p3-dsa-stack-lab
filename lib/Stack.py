class Stack:

    def __init__(self, items = [], limit = 100):
        pass
        self.items = items
        self.limit = limit

    def isEmpty(self):
        pass
        return self.size() == 0

    def push(self, item):
        pass
        if not self.full():
            self.items.append(item)

    def pop(self):
        pass
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        pass
        if not self.isEmpty():
            return self.items[-1]
    
    def size(self):
        pass
        return len(self.items)

    def full(self):
        pass
        return self.size() == self.limit

    def search(self, target):
        pass
        position = 0
        for index in range(self.size() - 1, -1, -1):
            if self.items[index] == target:
                return position
            position += 1
        return -1