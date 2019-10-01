class rock:
    x=4
f=rock()    
print(f.x)


class person:
    def __init__(obj,name,age):
        obj.name=name
        obj.age=age

    def func(a):
        print("my name is: "+a.name)
        print(a.age)
p1=person("john",33)
p1.func()


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=person("john",44)
print(p.name)
print(p.age)

