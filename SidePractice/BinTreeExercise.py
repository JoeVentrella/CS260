def buildTree(root):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def setLeftChild(self, newNode):
        if self.leftChild == None:
            self.leftChild = buildTree(newNode)
        else:
            t = buildTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def setRightChild(self, newNode):
        if self.rightChild == None:
            self.rightChild = buildTree(newNode)
        else:
            t = buildTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, newObj):
        self.key = newObj



ttree = buildTree('a')
ttree.setLeftChild('b')
