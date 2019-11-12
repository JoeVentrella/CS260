def binarySearch(aList, item):
    first  0
    last = len(aList) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if aList[midpoint] == item:
            found = True
        else:
            if item < aList[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return  found

testL = [0,1,2,8,13,17,19,32,42]
print(binarySearch(testL, 2))