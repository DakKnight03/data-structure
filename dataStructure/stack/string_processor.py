from lessons.dataStructure.stack import Stack

class StringProcessor:
    def reverse(self, string):
        stack = Stack()
        for i in string:
            stack.push(i)
        res = ""
        while not stack.is_empty():
            res += stack.pop()
        return res

    def binary_string(self, number):
        stack = Stack()
        while True:
            stack.push(number % 2)
            number = number // 2
            if number // 2 != 0:
                stack.push(number % 2)
                break
        res = ""
        while not stack.is_empty():
            res += str(stack.pop())
        return res

    def is_balance(self, bracket):
        stack = Stack()
        count = 0
        open_brack = ['(', '[', '{']
        close_brack = [')', ']', '}']
        close_list = []
        for i in bracket:
            if i in open_brack:
                stack.push(i)
            elif i in close_brack:
                if stack.is_empty():
                    return False
                last_open = stack.pop()
                if close_brack.index(i) == open_brack.index(last_open):
                    count += 1
                else:
                    return False
        if count == len(bracket) / 2:
            return True
        return False

binary = StringProcessor()
print(binary.is_balance("()()()()()"))