thisdict = {
    "brand":"ford",
    "model":"mustang",
    "year": 1964
}
if "model" in thisdict:
    print("yes, 'model' is one of the keys in the thisdict ... ")


print(len(thisdict))


thisdict = {
    "brand":"ford",
    "model":"mustang",
    "year": 1964
}
thisdict["color"]="red"
print(thisdict)


thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)


del thisdict ["brand"]
print(thisdict)

#error output
#del thisdict
#print(thisdict)



thisdict.clear()
print(thisdict)








