# len: shows number of element
list1=['march','april','may']
print(len(list1))

#append: add element after last one
list1=['march','april','may']
list1.append('june')
print(list1)

#insert: add element where you choose
list1=['march','april','may']
list1.insert(0,'february')
print(list1)

#remove()
list1=['march','april','may']
list1.remove('may')
print(list1)

list1=['march','may','april','may']
list1.remove('may')
print(list1)

#pop()
list1=['march','april','may']
list1.pop(1)
print(list1)

list1=['march','april','may']
list1.pop()
print(list1)

#clear()
list1=['march','april','may']
list1.clear()
print(list1)

#copy()
list1=['march','april','may']
list2=list1.copy()
print(list2)

#list()
list1=['march','april','may']
newlist=list(list1)
print(newlist)

list1 = list(("march","april","may"))
print(list1)


