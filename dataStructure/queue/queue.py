class Queue:

    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
    
    def __str__(self):
        res = ""
        for i in self.items:
            res += str(i) + " "
        res = res[:-1]
        return res

    def is_empty(self):
        return self.items == []

    def insert(self, string):
        if len(self.items) < self.capacity:
            self.items.insert(0, string)
            return True
        else:
            return False

    def remove(self):
        return self.items.pop(-1)

    def is_full(self):
        return len(self.items) == self.capacity