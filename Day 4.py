import random

#type() fuction

x=1 #int
y=2.8 #float
z=1j #complex
print(type(x))
print(type(y))
print(type(z))

#int 
x=1
y=359493
z=-9494
print(type(x))
print(type(y))
print(type(z))

#float
x=1.10
y=1.0
z=-43.21
print(type(x))
print(type(y))
print(type(z))

s=35e3
r=12E55
t=-43.1e43
print(type(s))
print(type(r))
print(type(t))

#complex
x=3+5j
y=5j
z=-5j
print(type(x))
print(type(y))
print(type(z))

#converting
x=1 #int
y= 2.8 # float
z=5j #complex
#int to float
a=float(x)
#float to int
b=int(y)
#int to complex
c=complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random()
print(random.randrange(1,10))


