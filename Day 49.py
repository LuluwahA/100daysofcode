x=300
def myfun():
    x=200
    print(x)
myfun()
print(x)

def myfun():
    global x
    x=300
myfun()
print(x)


x=300
def myfun():
    global x
    x=200
myfun()
print(x)
