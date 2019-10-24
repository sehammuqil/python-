import re

str = "the rain in spain"
x = re.sub("\s","9",str)
print(x)

#________________________

import re

str = "the rain in spain"
x = re.sub("\s","9",str,2)
print(x)

#___________________

import re

str = "the rain in spain"
x = re.search("ai",str)
print(x)


#__________________________

import re

str = "the rain in Spain"
x = re.search(r"\bS\w+",str)
print(x.span())

#____________________________


import re

str = "the rain in Spain"
x = re.search(r"\bS\w+",str)
print(x.string)


#______________________


import re

str = "the rain in Spain"
x = re.search(r"\bS\w+",str)
print(x.group())

#______________________
