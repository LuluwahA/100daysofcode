myset={}
print(myset)

myset={"may", "april","march"}
print(myset)

myset={"may", "april","march", 1,2,3,1}
print(myset)

myset={"may", "april","march"}
for x in myset:
    print(x)

myset={"may", "april","march"}
print("april" in myset)

myset={"may", "april","march"}
myset.add("june")
print(myset)

myset={"may", "april","march"}
myset.update(["june","july","october"])
print(myset)

