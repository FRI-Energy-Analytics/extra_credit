#!/bin/python3

# Recursion: Davis' Staircase
# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
# new solution uses dynamic programming!
# thanks jerry!
def stepPerms(n, memo={0: 1}):
    if(n<=0):
        if(n<0):
          return 0
        else:
          return 1
    elif n in memo.keys():
        return memo[n]
    else:
        memo[n-3] = stepPerms(n-3, memo)
        memo[n-2] = stepPerms(n-2, memo)
        memo[n-1] = stepPerms(n-1, memo)
        memo[n] = memo[n-3] + memo[n-2] + memo[n-1]
        return memo[n]

s = int(input())
for s_itr in range(s):
    n = int(input())
    print(stepPerms(n))
