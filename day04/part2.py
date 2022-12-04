import time

t1 = time.time()

count = 0

with open('input.txt') as f:
    for line in f:
        p = [list(map(int, line.split(",")[x].split("-"))) for x in range(2)]
        # if len(set(range(p[0][0], p[0][1] + 1)) & set(range(p[1][0], p[1][1] + 1))) > 0:
        #    count += 1
        o = [p[y][0] <= p[1^y][x] <= p[y][1] for x in range(2) for y in range(2)]
        if True in o:
            count += 1


print(count)

t2 = time.time()
print(t2-t1)

print(1^0)