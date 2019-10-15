import random
import timeit

exampleList = list(range(10000))
num = 10000

def bigOForListIndex(exampleList, n):
    """
    Experiment to verify list index is O(1)
    """
    for i in range(num):
        index = random.randint(0, num-1)
        exampleList[index]
def main():

    for n in range(1000000, 10000001, 1000000):
        exampleList = list(range(n))
        indexTime = timeit.Timer("bigOForListIndex(exampleList,"+str(n)+")",
                                 "from __main__ import exampleList,\
                                 bigOForListIndex")
        it = indexTime.timeit(number=1)
        print ("Length of time for %d index access in %d list of"\
               "numbers :%15.9f seconds" % (num, n, it))

if __name__ == '__main__':

    main()