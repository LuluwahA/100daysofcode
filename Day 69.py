f=open("demofile.txt")
f=open("demofile.txt","rt")

f=open("demofile.txt","r")
print(f.read())

f=open("demofile.txt","r")
print(f.read(9))

f=open("demofile.txt","r")
print(f.readline())

f=open("demofile.txt","r")
print(f.readline())
print(f.readline())


f=open("demofile.txt","r")
for x in f:
    print(x)

f=open("demofile.txt","r")
print(f.readline())
f.close()

f=open("demofile.txt","a")
f.write(" this is more text ")
f.close()

f=open("demofile.txt","r")
print(f.read())

f=open("demofile.txt","w")
f.write("deleted content")
f.close()
f=open("demofile.txt","r")
print(f.read())

f=open("testfile.txt","x")

import os
os.remove("demofile.txt")

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("this file does not exist")

import os
os.rmdir("myfolder")

