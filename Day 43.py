class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

x=person("john","bov")
x.printname()



class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

class stud(person):
    pass

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
        person.__init__(self,fname,lname)

x=stud("kyle","martins")
x.printname()
