# Last in - First Out (LIFO)

# n is any variable
# O(1), O(log(n)), O(n), O(n^2), 0(n^3), ...., O(exp(n)), O(exp(exp(n)), O(n!)

# (100):

class Stack():
    # Space complexity O(n)
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, value):
        # O(1)
        self.items.append(value)
        self.size += 1

    def pop(self):
        # O(1)
        last_val = self.items[-1]
        self.size -= 1
        del self.items[-1]
        return last_val

    def len(self):
        # 0(1)
        return self.size


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
