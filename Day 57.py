import re
t="the rain in spain"
x=re.search("^the.*spain$",t)
if(x):
    print("yes its a match")
else:
    print("no match")
    

import re
t="the rain in spain"
x=re.search("\Athe",t)
if(x):
    print("yes its a match")
else:
    print("no match")
    
import re
t="the rain in spain"
x=re.search("\s",t)
if(x):
    print("yes its a match")
else:
    print("no match")
    
