import re
str ="the rain in spain"
x=re.findall("ai",str)
print(x)

import re
str="the rain in spain"
x=re.findall("portugal",str)
print(x)

if(x):
    print("yes its a match")
else:
    print("no match")
    
import re
str="the rain in spain"
x=re.search("\s",str)
print("the first position :",x.start())


import re
str="the rain in spain"
x=re.search("portugal",str)
print(x)

import re
str="the rain in spain"
x=re.split("\s",str)
print(x)
