import json
x={
   "name":"john",
   "age":23,
   "married":True,
   "divorced":False,
   "children":("anna","jack"),
   "pets":None,
   "cars":[
       {"models":"BMW","mpg":32.49}
       ]
    }
print(json.dumps(x,indent=4))

import json
x={
   "name":"john",
   "age":23,
   "married":True,
   "divorced":False,
   "children":("anna","jack"),
   "pets":None,
   "cars":[
       {"models":"BMW","mpg":32.49}
       ]
    }
print(json.dumps(x,indent=4,separators=(".","=")))

import json
x={
   "name":"john",
   "age":23,
   "married":True,
   "divorced":False,
   "children":("anna","jack"),
   "pets":None,
   "cars":[
       {"models":"BMW","mpg":32.49}
       ]
    }
print(json.dumps(x,indent=4,sort_keys=True))
