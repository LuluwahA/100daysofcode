import re
str="the rain in spain"
x=re.sub("\s","9",str)
print(x)

import re
str="the rain in spain"
x=re.sub("\s","9",str,2)
print(x)

import re
str="the rain in spain"
x=re.search("ai",str)
print(x)

import re
str="the rain in spain"
x=re.search(r"\bs\w+",str)
print(x.span())

import re
str="the rain in spain"
x=re.search(r"\bs\w+",str)
print(x.string)

import re
str="the rain in spain"
x=re.search(r"\bs\w+",str)
print(x.group())
