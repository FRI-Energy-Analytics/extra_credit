import os
import sys

n, m = map(int, input().split())
coords = [[] for i in range(m)]

for i in range(n):
    a = map(int, input().split())
    for idx, x in enumerate(a):
        coords[idx].append(x)

result = []
for i in range(m):
    coords[i].sort()
    result.append(str(coords[i][(n-1)//2]))
print(" ".join(result))