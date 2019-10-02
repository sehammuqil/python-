def num(x,y):
    if (x > 0) :
        resulte = x ** y
    else:
        resulte = 0
        return resulte
    print (num(5,3))



num = [-4 , -6 , -5 ,-1 , 2 ,3 , 7 ,9 ,88]
for n in num :
    x = lambda z : print(z)if z > 0 else None
    x(n)