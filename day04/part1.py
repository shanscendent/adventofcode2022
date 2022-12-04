import time

t1 = time.time()

count = 0

with open('input.txt') as f:
    for line in f:
        p = [list(map(int, line.split(",")[x].split("-"))) for x in range(2)]
        if (p[0][0] - p[1][0]) * (p[0][1] - p[1][1]) <= 0:
            count += 1

print(count)

t2 = time.time()
print(t2-t1)
