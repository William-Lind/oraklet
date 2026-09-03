import random

datorn = random.randint(1,14)
människa = random.randint(1,14)

print (f"du slog {människa}")
print (f"datorns slog {datorn}")

if människa > datorn:
    print ("du slog roboten")
elif människa == datorn:
    print ("ni båda förlorade")
elif människa < datorn:
    print ("du förlorade")