import random

my_list = [1, 2, 3, "xxx"]
my_things = []

while len(my_things) <= 20:
    chosen = random.choice(my_list[:-1])
    if chosen == 2:
        continue
    my_things.append(chosen)
    print(chosen)

