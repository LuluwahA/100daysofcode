price=49
txt="the price is {} dollars"
print(txt.format(price))

price=49
txt="the price is {:.2f} dollars"
print(txt.format(price))

q=4
itemno=543
price=21
order="i want {} pieces of item number {} for {:.2f} dollars"
print(order.format(q,itemno,price))

