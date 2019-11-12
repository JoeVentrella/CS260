def mergeSort(aList):
    print("Splitting list", aList)
    if len(aList) > 1:
        mid = len(aList)//2
        leftHalf = aList[:mid]
        rightHalf = aList[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                aList[k] = leftHalf[i]
                i += 1
            else:
                aList[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            aList[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            aList[k] = rightHalf[j]
            j += 1
            k += 1
    print("Merge time", aList)

aList = [54,26,93,17,77,31,44,55,20]
mergeSort(aList)
print(aList)