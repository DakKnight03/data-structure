class Stack:
    def __init__(self):
        self.items = []
    def __str__(self):
        res = ""
        for i in self.items:
            res += str(i) + " "
        res = res[:-1]
        return res

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop(-1)
    
    def clear(self):
        self.items = []

    def is_empty(self):
        return self.items == []