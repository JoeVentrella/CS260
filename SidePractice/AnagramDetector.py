def anagramSolution(firstString, secondString):
    isOk = True
    if len(firstString) != len(secondString):
        isOk = False

    aList = list(secondString)
    position1 = 0

    while position1 < len(firstString) and isOk:
        position2 = 0
        found = False
        while position2 < len(aList) and not found:
            if firstString[position1] == aList[position2]:
                found = True
            else:
                position2 = position2 + 1

        if found:
            aList[position2] = None
        else:
            isOk = False

        position1 = position1 + 1

    return isOk

print(anagramSolution("abcd","dcbam"))

def anagramSolution2(stringOne, stringTwo):
    listOne = list(stringOne)
    listTwo = list(stringTwo)
    listOne.sort()
    listTwo.sort()
    pos = 0
    matches = True

    while pos < len(stringOne) and matches:
        if listOne[pos] == listTwo[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches
print(anagramSolution2('abcdefg', 'bcdfega'))

def bestAnagramSolution(str1, str2):
    counter1 = [0] * 26
    counter2 = [0] * 26

    for i in range(len(str1)):
        position = ord(str1[i]) - ord('a')
        counter1[position] = counter1[position] + 1

    for i in range(len(str2)):
        position = ord(str2[i]) - ord('a')
        counter2[position] = counter2[position] + 1

    j = 0
    stillOk = True
    while j < 26 and stillOk:
        if counter1[j] == counter2[j]:
            j = j + 1
        else:
            stillOk = False

        return stillOk

print(bestAnagramSolution('potatoe', 'toetapo'))