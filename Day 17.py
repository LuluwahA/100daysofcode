thistuple = ("apple", "orange", "cherry")
if "apple" in thistuple:
    print("YES, apple is in thistuple")

#return ("apple","apple","apple","apple")
thistuple = ("apple",)*4
print(thistuple)
#return appleappleappleapple
thistuple = ("apple")*4 
print(thistuple)

thistuple = ("apple", "orange", "cherry")
thistuple2= (1,2,3)
sumtuple=thistuple+thistuple2
print(sumtuple)

#return (3,4,5,6,1,2,3)
x=(3,4,5,6)
x=x+(1,2,3)
print(x)

thistuple = ("apple", "orange", "cherry")
print(len(thistuple))

thistuple=tuple(("apple", "orange", "cherry"))
print(thistuple)

thislist =[3,4,5,6,"A","B"]
thistuple=tuple(thislist)
print(thistuple)
