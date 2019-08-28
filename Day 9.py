age = 30
txt="My name is Lulu, and I am" +age
print(txt)


age = 30
txt="My name is Lulu, and I am {}"
print(txt.format(age))

q=3
item=345
price=49.95
myorder="i want {} pieces of item {} for {} dollars"
print(myorder.format(q,item,price))

q=3
item=345
price=49.95
myorder="i want to pay {2} dollars for {0} pieces of of item {1}"
print(myorder.format(q,item,price))
