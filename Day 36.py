def myfun(n):
    return lambda a:a*n
mydoubler=myfun(2)
print(mydoubler(11))


def myfun(n):
    return lambda a:a*n
mydoubler=myfun(2)
mytr=myfun(3)
print(mydoubler(11))
print(mytr(11))
