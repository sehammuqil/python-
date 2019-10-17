import mymodule as mx

a = mx.person1["age"]
print(a)

#____________

import platform

x=platform.system()
print(x)


#____________

import platform
print(platform.python_version())


#__________

import platform
x= dir (platform)
print(x)

#_________

from mymodule import person1
print(person1["age"])

#________