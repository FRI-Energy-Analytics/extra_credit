n = int(input())
A = [int(i) for i in input().split()]
m = int(input())
B = [int(i) for i in input().split()]
vals = {}
for i in A:
    if i not in vals:
        vals[i] = -1
    else:
        vals[i] -= 1
for i in B:
    if i not in vals:
        vals[i] = 1
    else:
        vals[i] += 1
pos = []
for i in vals:
    if vals[i] > 0:
        pos.append(i)
pos.sort()
for i in pos:
    print(i,end=' ')
