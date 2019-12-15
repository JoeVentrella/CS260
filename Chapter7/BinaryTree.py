class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


"""
Is there A More EFFICIENT way to access nodes lower down the tree???
"""
"""
ttree = BinaryTree('a')
ttree.insertLeft('b')
ttree.insertRight('c')
ttree.getLeftChild().insertRight('d')
ttree.getRightChild().insertLeft('e')
ttree.getRightChild().insertRight('f')
print(ttree.getRootVal())
print(ttree.getLeftChild().getRootVal())
print(ttree.getRightChild().getRootVal())
print(ttree.getLeftChild().getRightChild().getRootVal())
print(ttree.getRightChild().getLeftChild().getRootVal())
print(ttree.getRightChild().getRightChild().getRootVal())
"""
