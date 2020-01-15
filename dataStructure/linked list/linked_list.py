class Node:
    def __init__(self, content, next_node=None):
        self.content = content
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head == None:
            return "<<E>>"
        else:
            path = ""
            steps = self.head
            while steps != None:
                path += str(steps.content) + "->"
                steps = steps.next
            path = path[:-2]
            return path

    def add_first(self, content):
        node = Node(content, self.head)
        self.head = node
        
    def remove_first(self):
        if self.head == None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp

    def add_last(self, content):
        if self.head == None:
            self.add_first(content)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            node = Node(content)
            current.next = node

    def remove_last(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            return self.remove_first()
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            temp = current.next
            current.next = None
            return temp

    def find(self, value):
        current = self.head
        while current != None:
            if current.content == value:
                return current
            current = current.next
        return None