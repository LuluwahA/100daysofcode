x=1
while x<6:
    print(x)
    x+=1

    
x=1
while x<6:
    print(x)
    if x==3:
        break
    x+=1

x=1
while x<6:
    x+=1
    if x==3:
        continue
    print(x)   

x=1
while x<10:
    print(x)
    x+=1
else:
    print("x is no longer less than 10")
