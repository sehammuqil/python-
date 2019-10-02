class Myclass :
 x = 5
print(Myclass)



class Myclass:
    x = 5
p1 = Myclass()
print(p1.x)


class person:
    def __init__(mysillyobject , name , age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("hello my name is "+ abc.name)
p1 = person("john",36)
p1.myfunc()




class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
p1 = person("john", 36)
print(p1.name)
print(p1.age)





