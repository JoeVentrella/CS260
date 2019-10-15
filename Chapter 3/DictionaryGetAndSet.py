import timeit

Dictionary = {}

def timeDictSetFn(n):
    global Dictionary

    for i in range(n):
        Dictionary[i] = i

def timeDictGetFn(n):
    global Dictionary

    for i in range(n):
        x = Dictionary[i]

def main():
    k = 10

    print("This checks the amount of time to use set for dictionaries: ")

    for n in range(100000, 1000001, 100000):
        setTime = timeit.Timer("timeDictSetFn(" + str(n) + ")",

                               "from __main__ import timeDictSetFn")

        sit = setTime.timeit(k)

        print("Amount of time to do {} dictionary inserts: {}".format(n, sit))
        print("Amount of time to do {} dictionary inserts: {}".format(1, sit / float(k * n)))
    print("This checks the dictionary get times: ")

    for n in range(100000, 1000001, 100000):
        setTime = timeit.Timer("timeDictSetFn(" + str(n) + ")",
                               "from __main__ import timeDictSetFn")
        getTime = timeit.Timer("timeDictGetFn(" + str(n) + ")",
                               "from __main__ import timeDictGetFn")

        git = getTime.timeit(k)
        print("Amount of time to do {} dictionary gets: {}".format(n, git))
        print("Amount of time to do {} dictionary gets: {}".format(1, git / float(k * n)))

if __name__ == '__main__':
    main()
