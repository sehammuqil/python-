import re

str = "the rain in spain"
x = re.findall("ai",str)
print(x)

#______________________

import re
str = "the rain in spain"

x= re.findall("portugal", str)
print(x)

if (x):
    print("yes,there is at least one match!")
else:
    print("no match")

#______________________________

import re

str = "the rain in spain"
x = re.search("\s",str)
print("the frist white-space character is located in position:",x.start())


#_____________________________________

import re

str = "the rain in spain "
x = re.search("portugal" , str)
print(x)

#________________________


import re
str = "the rain in spain"
x = re.split("\s",str)

print(x)


#______________________



