f=["apple","banana","cherry"]
for x in f:
    print(x)
for x in "banana":
    print(x)

f=["apple","banana","cherry"]
for x in f:
    print(x)
    if x == "banana":
        break

    
f=["apple","banana","cherry"]
for x in f:
    if x == "banana":
        break
    print(x)

f=["apple","banana","cherry"]
for x in f:
    if x == "banana":
        continue
    print(x)
