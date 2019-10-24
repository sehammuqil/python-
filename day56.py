
import json

x = {
    "name":"john",
    "age":30,
    "married" : True ,
    "divorced": False ,
    "children":("ann","billy"),
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":27.5},
        {"model":"ford edge","mpg":24.1}
    ]

}
print(json.dumps(x,indent=4))


#______________________________________


import json

x = {
    "name":"john",
    "age":30,
    "married" : True ,
    "divorced": False ,
    "children":("ann","billy"),
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":27.5},
        {"model":"ford edge","mpg":24.1}
    ]

}
print(json.dumps(x,indent=4,separators=("."," = ")))


#_____________________________________


import json

x = {
    "name":"john",
    "age":30,
    "married" : True ,
    "divorced": False ,
    "children":("ann","billy"),
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":27.5},
        {"model":"ford edge","mpg":24.1}
    ]

}
print(json.dumps(x,indent=4,sort_keys=True))

#____________________________________

