def factorialRec(num):
    """
    :param num: Takes an int
    :return: The factorial of the int input
    """
    if num <= 1:
        return 1

    return num * factorialRec(num - 1)


def readInput():
    """
    :return: The number input by the user
    """
    while True:
        num = input("Please input number to calculate fac of: ")
        num = num.strip()

        if num.isdigit():
            num = int(num)

            return num
        else:

            print("Bad Input. Try again..")


def main():
    num = readInput()
    fact = factorialRec(num)
    print("Factorial of %d is: %d" % (num, fact))


if __name__ == '__main__':
    main()
