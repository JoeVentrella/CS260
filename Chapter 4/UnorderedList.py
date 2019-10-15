class Node:

    def __init__(self, initdata):
        self.data = initdata

        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):

        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)

        if self.tail == None:
            self.tail = temp
        self.head = temp

    def size(self):

        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):

        current = self.head
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):

        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True

            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()

        else:
            previous.setNext(current.getNext())

    def append(self, item):

        current = self.tail
        temp = Node(item)
        current.setNext(temp)


mylist = UnorderedList()

mylist.add(11)
mylist.add(7)
mylist.add(1)
mylist.add(83)
mylist.add(22)
mylist.add(45)
print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
mylist.add(100)
print(mylist.search(100))
print(mylist.size())
mylist.remove(45)
print(mylist.size())
mylist.remove(11)
print(mylist.size())
mylist.remove(1)
print(mylist.size())
print(mylist.search(7))
mylist.append(123)
print(mylist.size())