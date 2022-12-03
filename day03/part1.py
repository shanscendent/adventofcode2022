import time

t1 = time.time()

priority = 0

with open('input.txt') as f:
    for rucksack in f:
        c1 = rucksack[:len(rucksack)//2]
        c2 = rucksack[len(rucksack)//2:]
        pi = set(c1).intersection(c2).pop()
        if pi.islower():
            priority += ord(pi) - 96
        else:
            priority += ord(pi) - 38

print(priority)

t2 = time.time()
print(t2-t1)
