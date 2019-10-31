class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def rev_string(myString):
    stac = Stack()
    for char in myString:
        stac.push(char)
    revStr = ''
    while not stac.isEmpty():
        revStr = revStr + stac.pop()
    return revStr


def matches(open,close):
    opens = "({["
    closers = ")}]"
    return opens.index(open) == closers.index(close)


def parChecker(symbolString):
    stc = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({[":
            stc.push(symbol)
        else:
            if stc.isEmpty():
                balanced = False
            else:
                top = stc.pop()
                if not matches(top,symbol):
                    balanced = False
        index += 1
    if balanced and stc.isEmpty():
        return True
    else:
        return False


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString





def main():
    x = 20
    s = Stack()
    s.push(x)
    s.push(13)
    s.push('dog')
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(rev_string('Joseph'))

    print(parChecker("{({([][])}())}"))
    print(parChecker('({[)}]'))
    print(divideBy2(42))



if __name__ == '__main__':
    main()