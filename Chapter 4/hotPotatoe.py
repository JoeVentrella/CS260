from Queue import Queue

def hotPotato(listName, number):
    simulateQue = Queue()
    for name in listName:
        simulateQue.enqueue(name)

    while simulateQue.size() > 1:
        for i in range(number):
            simulateQue.enqueue(simulateQue.dequeue())

        simulateQue.dequeue()

    return simulateQue.dequeue()


print(hotPotato(["Joe", "Elena", "Stef", "Bob", "Nan", "Ryan"], 7))
