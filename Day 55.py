# json to python
import json
x='{"name":"john", "age":12 ,"city":"riadh"}'
y=json.loads(x)
print(y["age"])
# python to json
import json
x={"name":"john", "age":12,"city":"riadh"}
y=json.dumps(x)
print(y)

import json
print(json.dumps({"name":"john", "age":12,"city":"riadh"}))
print(json.dumps(["hi","there"]))
print(json.dumps(("john","osman")))
print(json.dumps("hi"))
print(json.dumps(43))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
