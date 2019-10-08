mytup=("apple","banana","cherry")
x=iter(mytup)
print(next(x))
print(next(x))
print(next(x))

x="banana"
y=iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

mytup=("apple","banana","cherry")
for x in mytup:
    print(x)

x="banana"
for y in x:
    print(y)

class mynumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
       x=self.a
       self.a+=1
       return x

myclass=mynumber()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class mynumber:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
      if self.a<=20:
        x=self.a
        self.a+=1
        return x
      else:
          raise StopIteration

myclass=mynumber()
myiter=iter(myclass)

for x in myiter:
    print(x)


