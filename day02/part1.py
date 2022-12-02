import time

t1 = time.time()

score = 0

with open('input.txt') as f:
    for r in f:
        p1, p2 = ord(r[0]), ord(r[2])
        score += (p2 - 87) + (p2 - p1 - 22) % 3 * 3
        
print(score)

t2 = time.time()
print(t2-t1)
