myset={"march", "april","may"}
print(len(myset))

myset={"march", "april","may"}
myset.remove("may")
print(myset)

myset={"march", "april","may"}
myset.discard("may")
print(myset)

myset={"march", "april","may"}
x=myset.pop()
print(x)
print(myset)

myset={"march", "april","may"}
myset.clear()
print(myset)

myset=set(("march", "april","may"))
print(myset)

myset={"march", "april","may"}
del myset
print(myset)

