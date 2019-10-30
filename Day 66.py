q=4
itemno=543
price=21
order="i want {0} pieces of item number {1} for {2:.2f} dollars"
print(order.format(q,itemno,price))


age=42
name="john"
txt="his name is {1}. {1} is {0} years old"
print(txt.format(age,name))

order="i have a {carname}, it is a {model}"
print(order.format(carname="ford", model="mustang"))
