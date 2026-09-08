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
print (f"Dealerns första kort är {dataett}")

öka = input("vill du höja eller stanna höj/stanna ")

if öka == ("höj"):
    print (summatvå)
    if summatvå == 21:
        print ("du vann")
    elif summatvå > 21:
        print ("du förlorade")
    elif summatvå > datorsumma:
        print ("du vann!")
    elif summatvå < datorsumma:
        print ("du förlorade")
elif öka ==("stanna"):
    print (summa)
    if summa == 21:
        print ("du vann!")
    elif summa > 21:
        print ("du förlorade")
    elif summa > datorsumma:
        print ("du vann!")
    elif summa < datorsumma:
        print ("du förlorade")
