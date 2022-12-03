import time

t1 = time.time()

priority = 0
group = []

with open('input.txt') as f:
    for count, rucksack in enumerate(f):
        group.append(rucksack.strip())
        if count % 3 == 2:
            badge = (set(group[0]) & set(group[1]) & set(group[2])).pop()
            group = []
            if badge.islower():
                priority += ord(badge) - 96
            else:
                priority += ord(badge) - 38

print(priority)

t2 = time.time()
print(t2-t1)
