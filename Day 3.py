Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> y = "john"
>>> print(x)
5
>>> print(y)
john
>>> x = 4 #x is type of int
>>> x = "sally" #x is now type of string
>>> print(x)
sally
>>> x ='john'
>>> print(x)
john
>>> x = "john"
>>> print(x)
john
>>> x,y,z = "ornage", "banana", "cherry"
>>> print(x)
ornage
>>> print(y)
banana
>>> print(z)
cherry
>>> x=y=z="orange"
>>> print(x)
orange
>>> print(y)
orange
>>> print(z)
orange
>>> x = "awesome"
>>> print("python is "+ x)
python is awesome
>>> x ="python is "
>>> y="awesome"
>>> z=x+y
>>> print(z)
python is awesome
>>> x=1
>>> y=2
>>> print(x+y)
3
>>> x=3
>>> y="john"
>>> print(x+y)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(x+y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
