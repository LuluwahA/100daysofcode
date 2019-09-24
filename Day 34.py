def myfun(food):
    for x in food:
        print(x)
fruits =["apple","banana","cherry"]
myfun(fruits)


def myfun(x):
    return 5*x
print(myfun(3))
print(myfun(5))
print(myfun(9))

def myfun(c1,c2,c3):
    print("the youngest child is "+c3)
myfun(c1="emily",c2="toby",c3="linus")

def myfun(*kids):
    print("the youngest child is "+kids[2])
myfun("emily","toby","kimy")

def tri(k):
    if(k>0):
        result=k+tri(k-1)
        print(result)
    else:
        result=0
    return result
print("\n recursion example result")
tri(6)
