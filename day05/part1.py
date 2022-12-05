import time
import re

t1 = time.time()

mode = 0

with open('input.txt') as f:
    length = len(f.readline().strip("\n"))
    stacks = [[] for x in range((length + 1) // 4)]
    f.seek(0)
    for line in f:
        if mode == 0:
            if line == "\n":
                mode = 1
                for stack in stacks:
                    stack.pop()
                    stack.reverse()
                continue
            for stack, crate in enumerate(line[2 - 1::4]):
                if not crate == " ":
                    stacks[stack].append(crate)
        else:
            pass
            x = [x - 1 for x in map(int, re.findall('[0-9]+', line))]
            for i in range(x[0] + 1):
                stacks[x[2]].append(stacks[x[1]].pop())

rearranged = []

for stack in stacks:
    rearranged.append(stack.pop())

print("".join(rearranged))

t2 = time.time()
print(t2-t1)
