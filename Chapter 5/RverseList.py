def reverseList(j):
    """Funcction that takes a list and reverses it"""
    if len(j) <= 1:
        return j[0]
    else:
        return reverseList(j[1:]) + j[0]

print(reverseList("hello"))