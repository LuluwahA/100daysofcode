class library:
    def __init__(self, book, shelf):
        self.book=book
        self.shelf=shelf
x=library(300,45)
print("Number of Books: ",x.book,
      "and Number of shelfs is: ",x.shelf)

class science_section:
    def __init__(self,book,shelf,name):
        super().__init__(book,shelf)
        self.name=name
    def print1(self):
        print("Number of Books: ",self.book,
      "and Number of shelfs is: ",self.shelf,
              "Section: ",self.name)
    y=science_section(20,4,"physics books")
    y.print1()
