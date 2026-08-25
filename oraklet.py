import random

svar = ["Ja, helt klart.", "Absolut inte", "fråga igen imorgon", "Det vill du inte veta", "Sorry i cannot fufill this request"]


fråga = input("Fråga oraklet: ")
print("Du frågade:", fråga)
print(random.choice(svar))