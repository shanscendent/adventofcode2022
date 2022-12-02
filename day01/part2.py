import time

t1 = time.time()

elves = []

with open('input.txt') as f:
    lines = f.readlines()
    elf = 0
    for food in lines:
        if food.strip() == "":
            elves.append(elf)
            elf = 0
        else:
            elf += int(food)

elves.sort(reverse=True)

print(sum(elves[0:3]))

t2 = time.time()
print(t2-t1)