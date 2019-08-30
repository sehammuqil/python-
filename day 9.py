age = 36
txt = "my name is john , and i am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder= " i want {} pieces of item {} for {} dollars "
print(myorder.format(quantity,itemno,price))


myorder= " i want {2} pieces of item {1} for {0} dollars "
print(myorder.format(quantity,itemno,price))



