#!/bin/python3

# Recursion: Davis' Staircase
# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
def stepPerms(n):
    # this solution works but it times out :/
    if(n<0):
        return 0
    if(n==0):
        return 1
    else:
        return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)

s = int(input())
for s_itr in range(s):
    n = int(input())
    print(stepPerms(n))
