class TermNode:
    def __init__(self, coefficient, degree, next_node=None):
        self.coefficient = coefficient
        self.degree = degree
        self.next = next_node
    def evaluate(self, x):
        return (self.coefficient * (x ** self.degree))
    def __str__(self):
        if self.coefficient == 0:
            return ""
        if self.degree == 0:
            return str(self.coefficient)
        if self.coefficient == 1:
            return ("x^%d" % (self.degree))
        if self.degree == 1:
            return ("%dx" % (self.coefficient))
        return ("%dx^%s" % (self.coefficient, self.degree))


class Polynom:
    def __init__(self):
        self.head = None
    def __str__(self):
        polynom = ""
        steps = self.head
        while steps != None:
            polynom += steps.__str__() + "+"
            steps = steps.next
        polynom = polynom[:-1]
        print(polynom)
        return polynom
    def add(self, c, d):
        if self.head == None or self.head.degree < d:
            term_node = TermNode(c, d, self.head)
            self.head = term_node
        else:
            current = self.head
            while current.next != None:
                if current.degree < d:
                    break
                if current.degree == d:
                    current.coefficient += c
                    break
                current = current.next
            term_node = TermNode(c, d, current.next)
            current.next = term_node
    def evaluate(self, x):
        rel = 0
        steps = self.head
        while steps != None:
            rel += steps.evaluate(x)
            steps = steps.next
        return rel
    def derivate(self):
        res = Polynom()
        current = self.head
        while current != None:
            res.add(current.coefficient * current.degree, current.degree - 1)
            current = current.next
        return res