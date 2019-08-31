
#I to WE
x="Please, I want {} sandwishes and {} donutes"
print(x.replace("I","we"))


#format(5,7)
a=5
b=7
x="Please, I want {} sandwishes and {} donutes"
print(x.format(a,b))

#capital a
x="Please, I want {} sandwishes and {} donutes"
print(x.replace("a","A"))

#all modifications
x="Please, I want {} sandwishes and {} donutes"
print(x.replace("I","we").format(a,b).replace("a","A"))


