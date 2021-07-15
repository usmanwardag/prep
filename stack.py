# Last in - First Out (LIFO)


# O(1), O(n)

class Stack():
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        last_val = self.items[-1]
        del self.items[-1]
        return last_val

    def len(self):
        return len(self.items)


stack = Stack()
stack.push(3)
print(stack.items)
stack.push(4)
print(stack.items)
stack.push(5)
print(stack.items)
stack.pop()
print(stack.items)
stack.pop()
print(stack.items)
stack.pop()
print(stack.items)


# []
# push 3 -> [3]
# push 4 -> [3, 4]
# push 5 -> [3, 4, 5]
# pop    -> [3, 4]
# pop    -> [3]
