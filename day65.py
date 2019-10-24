price = 49
txt = "the price is {} dollars"
print(txt.format(price))

#____________________________

price = 49
txt = "the price is {:.2f} dollars"
print(txt.format(price))

#_____________________________

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity,itemno,price))