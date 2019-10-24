import json

x= '{"name":"john","age":30,"city":"new york"}'

y= json.loads(x)

print(y["age"])

#__________________________

import json
x = {
    "name":"john",
    "age":30,
    "city":"new york"
}
y = json.dumps(x)

print(y)

#________________________

print(json.dumps({"name":"john","age":30}))
print(json.dumps(["apple","bananas"]))
print(json.dumps(["apple","bananas"]))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


#_______________________

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

y = json.dumps(x)
print(y)

#________________________

