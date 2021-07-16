# First in - First Out (FIFO)


class Queue():
    # Space complexity O(n)
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, value):
        # O(n)
        self.items.append(-1)
        for idx in reversed(range(1, len(self.items))):
            self.items[idx] = self.items[idx-1]
        self.items[0] = value
        self.size += 1

    def dequeue(self):
        # O(1)
        last_val = self.items[-1]
        self.size -= 1
        del self.items[-1]
        return last_val

    def len(self):
        return self.size


queue = Queue()
queue.enqueue(3)
print(queue.items)
queue.enqueue(4)
print(queue.items)
queue.enqueue(5)
print(queue.items)
val = queue.dequeue()
print(f'{val} out. New queue items: {queue.items}')
val = queue.dequeue()
print(f'{val} out. New queue items: {queue.items}')
val = queue.dequeue()
print(f'{val} out. New queue items: {queue.items}')
