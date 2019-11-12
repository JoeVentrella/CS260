from Queue import Queue


def radixSort(nums):
    """
    :param nums: Takes a list of numbers as a string
    :return: Returns the numbers in ascending order
    """

    if nums is None or len(nums) < 1:
        return nums

    mainQ = Queue()
    binQs = []
    # Add all the numbers in the main Queue
    for n in nums:
        mainQ.enqueue(n)
    # create an array of Queues and initialize them - bin 0 to 9
    for i in range(10):
        binQs.append(Queue())
    # get the max length of digits in any input number - this will decide the
    # outer iteration we need to do in our radix sort implementation
    maxLen = len(nums[0])
    for i in range(1, len(nums)):
        if len(nums[i]) > maxLen:
            maxLen = len(nums[i])
    # we need to iterate maxLen times ie length of the biggest number (in
    # digits)

    for i in range(1, maxLen + 1):
        visited = []
        # below iteration includes only numbers of digit length i
        while not mainQ.isEmpty():
            val = mainQ.dequeue()
            if i > len(val):
                visited.append(val)
                continue
            r = val[-i]  # get the ith index from last
            r = int(r)
            binQs[r].enqueue(val)
        for v in visited:
            mainQ.enqueue(v)
        for i in range(10):
            while not binQs[i].isEmpty():
                mainQ.enqueue(binQs[i].dequeue())
    result = []

    while not mainQ.isEmpty():
        result.append(mainQ.dequeue())

    return result

def readInput():
    while True:
        print("Enter comma separated numbers: ")
        data = input()
        data = data.split(",")
        try:
            nums = [d.strip() for d in data]
            break
        except ValueError:
            print("Bad input, plz try again..")

    return nums

def printData(nums):
    if nums is None or len(nums) < 1:
        print("EMPTY LIST - Nothing to print!")
    else:
        for n in nums:
            print(n, end=" ")
    print()

def main():
    nums = readInput()
    nums = radixSort(nums)
    print("After applying radix sort: ")
    printData(nums)

if __name__ == '__main__':
    main()
