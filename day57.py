import re

txt = "the rain in spain"
x = re.search("^the.*spain$", txt)

if(x):
    print("YES! We have a mathch!")
else:
    print("No match")


#__________________________

