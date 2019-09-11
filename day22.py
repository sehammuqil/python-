thisdict = {}
print (thisdict)


thisdict = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(thisdict)
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)


thisdict["year"]=2018
print(thisdict)


for x in thisdict:
    print(x)


for x in thisdict:
    print(thisdict[x])


for x in thisdict.values():
    print(x)


print(thisdict.values())



for x , y in thisdict.items():
    print(x,y)


thisdict={"brand":"ford","model":"mustang","year":1964}
print(thisdict.items())














