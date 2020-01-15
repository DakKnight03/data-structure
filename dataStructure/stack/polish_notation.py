from lessons.dataStructure.stack import Stack

class PolishNotation:

    def calculate(self, string):
        num1 = 0
        num2 = 0
        stack = Stack()
        for i in string:
            if i == '+' or i == '-' or i == '*' or i == '/':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == '+':
                    stack.push(num1 + num2)
                if i == '-':
                    stack.push(num1 - num2)
                if i == '*':
                    stack.push(num1 * num2)
                if i == '/':
                    stack.push(num1 / num2)
            else:
                stack.push(i)
        
        return stack.pop()