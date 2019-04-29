import random

for x in range(10):
    print(random.randint(1,101))

# the above code will produce 10 numbers between 1 and 100. each will be printed on a new line...

# how to generate a LIST of random numbers?

rando_list = []

for x in range(10):
    y = random.randint(1,101)
    rando_list.append(y)

print(rando_list)
