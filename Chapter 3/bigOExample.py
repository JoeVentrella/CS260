from random import randrange
import time

def nSquared(aList):
    """" This function shows the runtime behavior of a function with runtime behavior of n^2"""
    smallestNum = aList[0]
    for i in aList:
        isSmallest = True
        for j in aList:
            if i > j:
                isSmallest = False
        if isSmallest:
            smallestNum = i
    return smallestNum

for listSize in range(1000,10000,1000):
    aList = [randrange(10000) for x in range(listSize)]
    start = time.time()
    print(nSquared(aList))
    end = time.time()
    print("size: %d time: %f " %(listSize, end-start))

def linear(aList):
    """
    :param Takes a list of numbers
    :return: Returns the smallest # in the list and the time to run f(x)
    """
    currentMin = aList[0]
    for i in aList:
        if i < currentMin:
            currentMin = i
    return currentMin

for listSize in range(1000,10000,1000):
    aList = [randrange(10000) for x in range(listSize)]
    start = time.time()
    print(linear(aList))
    end = time.time()
    print("size: %d time: %f" %(listSize, end-start))