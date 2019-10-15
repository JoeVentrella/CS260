class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

qu = Queue()
print(qu.isEmpty())
qu.enqueue(8)
qu.enqueue('Joe')
qu.enqueue(True)
print(qu.size())
print(qu.isEmpty())
qu.enqueue(2.4)
print(qu.dequeue())
print(qu.dequeue())
print(qu.size())

