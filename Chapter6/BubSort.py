def bubbleSort(alist):
    """Simple bubbleSort, Takes a list to sort"""
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


alist = [9,15,2,10,50,30,6,22,19,4]

bubbleSort(alist)

print(alist)