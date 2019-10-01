class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func(self):
        print("my name is: "+self.name)
p1=person("john",44)
p1.func()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func(self):
        print("my name is: "+self.name)
p1=person("john",44)
p1.age=33
print(p1.age)

"""class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func(self):
        print("my name is: "+self.name)
p1=person("john",44)
del p1.age
print(p1.age)"""

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func(self):
        print("my name is: "+self.name)
p1=person("john",44)
del p1
print(p1)
