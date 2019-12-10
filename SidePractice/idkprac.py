class Node:
    def __init__(self,initialData):
        self.data = initialData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        currentNode = self.head
        counter = 0
        while currentNode != None:
            counter += 1
            currentNode = currentNode.getNext()

        return counter

    def search(self, itemToFind):
        currentNode = self.head
        found = False
        while currentNode != None and not found
            if currentNode.getData() == itemToFind
                found = True
            else:
                currentNode = currentNode.getNext

        return found

    def remove(self,item):
        current = self.head
        prev = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                prev = current
                current = current.getNext()

        if prev == None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext)


