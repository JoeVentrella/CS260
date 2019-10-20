import time


def readInput():
    while True:
        number = input("Input number to calculate fibonacci of:  ")
        number = number.strip()
        if not number.isdigit():
            print("Bad input, enter integer")
            continue
        number = int(number)
        if number < 0:
            print("Bad do not input negative integers")
            continue
        return number


def fibonacci_iterative(num):
    """Calculates fib iteratively to show difference in iteration and recursion"""
    if num == 0 or num == 1:
        return num
    fib1 = 0
    fib2 = 1
    count = 2
    result = 1
    while count <= num:
        result = fib1 + fib2
        fib1, fib2 = fib2, result
        count += 1
    return result


def fibonacci_recursive(num):
    """Calculates fib recursively"""
    if num <= 1:
        return num
    if num >= 2:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)


def main():
    number = readInput()
    # first calculate fibonacci iteratively
    start = time.time()
    result = fibonacci_iterative(number)
    end = time.time()
    print("Fibonacci number %d is: %d in time(iterative): %f" %
          (number, result, round((end - start), 5)))

    # now calculate fibonacci recursively
    number = readInput()
    start = time.time()
    result = fibonacci_recursive(number)
    end = time.time()
    print("Fibonacci number %d is: %d in time(recursively): %f" %
          (number, result, round((end - start), 5)))


if __name__ == '__main__':
    main()
