
class person :
    def __init__(self , fname ,lname):
        self.firstname= fname
        self.lastname=lname

    def printname(self):
      print(self.firstname , self.lastname)

class student(person):
     def __init__(self , fname , lname):
       super().__init__(fname , lname)


x = student ("mike", "olsen")
x.printname()

#___________________________
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019


x = student("mike", "olsen")

print(x.graduationyear)



#_________________________________


class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class student(person):
    def __init__(self, fname, lname , year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = student("mike", "olsen",2019)

print(x.graduationyear)


#__________________________________


class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class student(person):
    def __init__(self, fname, lname , year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("welcome", self.firstname,self.lastname,"to the class of ",self.graduationyear)

x = student("mike", "olsen",2019)

x.welcome()
