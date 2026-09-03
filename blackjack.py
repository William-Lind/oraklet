import random

två = random.randint(1,11)
ett = random.randint(1,11)
tre = random.randint(1,11)
summa = ett + två
summatvå = summa + tre

dataett = random.randint(1,11)
datatvå = random.randint(1,11)
datorsumma = dataett + datatvå

print (f"{summa}")

höj = input("vill du ta ett till kort ja/stanna ")

if höj == ("ja"):
    print (summatvå)
elif höj ==("stanna"):
    print (summa)

if summa == 21:
    print ("du vann!")
elif summa > 21:
    print ("du förlorade")


if summatvå == 21:
    print ("du vann")
elif summatvå > 21:
    print ("du förlorade")