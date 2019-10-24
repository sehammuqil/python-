try:
    print(x)
except:
    print("An exception")

#__________________________________

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("something else went wrong")

#______________________________________

try:
    print("hello")
except:
    print("something went wrong ")
else:
    ("nothing went wrong")

#_____________________________

try:
    print("hello")
except:
    print("something went wrong ")
finally:
    print("the 'try except' is finished")

#________________________

