class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

class stud(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

x=stud("kyle","martins")
x.printname()



class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

class stud(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.grad=2019

x=stud("kyle","martins")
print(x.grad)



class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

class stud(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.grad=year

x=stud("kyle","martins", 2019)
print(x.grad)



class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

class stud(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.grad=year

    def welcome(self):
        print("welcome", self.firstname,self.lastname,"to the class of",self.grad)


x=stud("kyle","martins", 2019)
x.welcome()

