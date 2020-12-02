#!/bin/python3

import sys

N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]

loaves = 0
for i in range(N-1):
    if B[i]%2 == 1:
        B[i] += 1
        B[i+1] += 1
        loaves += 2

oddFlag = False       
for i in range(N):
    if B[i] %2 == 1:
        oddFlag = True  
        break

if not oddFlag:
    print(loaves)
else:
    print("NO")