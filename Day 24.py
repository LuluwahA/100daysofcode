thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1966 }
mydict=thisdict.copy()
print(thisdict)

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1966 }
mydict=dict(thisdict)
print(thisdict)

family={
"child1":{
    "name":"ahmed",
    "year":"2004"},
"child2":{
    "name":"osama",
    "year":"2007"},
"child3":{
    "name":"leen",
    "year":"2011"}
    }
print(family)


child1={
    "name":"ahmed",
    "year":"2004"},
child2= {
    "name":"osama",
    "year":"2007"},
child3={
    "name":"leen",
    "year":"2011"}
family={
    "child1": child1,
    "child2": child2,
    "child3": child3}
print(family)

thisdict = dict(brand="ford", model="mustang", year=1966)
print(thisdict)
