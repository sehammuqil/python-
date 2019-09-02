thislist=['apple','banana','cherry']
print(len(thislist))



thislist=['apple','banana','cherry']
thislist.append('orange')
print(thislist)



thislist=['apple','banana','cherry']
thislist.insert(1,"orange")
print(thislist)



thislist=['apple','banana','cherry']
thislist.remove("banana")
print(thislist)

thislist=['banana','apple','banana','cherry','banana']
thislist.remove("banana")
print(thislist)



thislist=['apple','banana','cherry']
thislist.pop()
print(thislist)

thislist=['apple','banana','cherry']
thislist.pop(1)
print(thislist)


thislist=['apple','banana','cherry']
thislist.clear()
print(thislist)



thislist=['apple','banana','cherry']
mynewlist = thislist.copy()
print(mynewlist)

thislist=['apple','banana','cherry']
mynewlist = thislist.copy()
thislist.pop(0)

print(mynewlist)
print(thislist)



thislist=['apple','banana','cherry']
mynewlist = thislist
thislist.pop(0)

print(mynewlist)
print(thislist)




thislist=['apple','banana','cherry']
mynewlist = list (thislist)
print(mynewlist)



thislist= list (('apple','banana','cherry'))
print(thislist)
























