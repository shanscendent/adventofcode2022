import time

t1 = time.time()

score = 0

with open('input.txt') as f:
    for r in f:
        p1, e = ord(r[0]), ord(r[2])
        score += (e - 88) * 3 + (p1 + e - 151) % 3 + 1
        
print(score)

t2 = time.time()
print(t2-t1)
