def seqSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


testlist = [9, 6, 10, 24, 6, 12, 14, 21, 99]

print(seqSearch(testlist, 5))

print(seqSearch(testlist, 24))
