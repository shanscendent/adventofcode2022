import time
import re

t1 = time.time()

n = 4

with open('input.txt') as f:
    buf = f.readline()

for i in range(len(buf)- n + 1):
    window = buf[i:i+n]
    if len(set(window)) == n:
        break

print(i+n)

t2 = time.time()
print(t2-t1)
