def recurBinarySearch(alist, item):
    """
    :param aList: Takes a list of numbers
    :param item: The nuber to find in the search
    :return: Returns a boolean True if found item False if not
    """
#This Search uses slice and is extremely ineficcient
    if len(alist) == 0:

        return False

    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:

            return True

        else:
            if item < alist[midpoint]:
                return recurBinarySearch(alist[:midpoint], item)
            else:
                return recurBinarySearch(alist[midpoint + 1:], item)


testlist = [0, 1, 9, 10, 24, 12, 7, 15 ]
print(recurBinarySearch(testlist, 6))
print(recurBinarySearch(testlist, 24))