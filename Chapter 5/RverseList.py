def reverseList(s):
    if len(s) <= 1:
        return s[0]
    else:
        return reverseList(s[1:]) + s[0]

print(reverseList("hello"))