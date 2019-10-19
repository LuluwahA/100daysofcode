#1
import json 
mytuple=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
x=json.dumps(mytuple)
print(x)

#2
import re
str = "data is the new oil"
x = re.search("data",str)
if (x):
    print("yes, data is a match ")
else:
    print("sorry it doesn't have that word")
