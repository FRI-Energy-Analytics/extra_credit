#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    dp = [0]*(k+1)
    dp[0] = 0
    for i in range(1, k+1):
        dp[i] = dp[i-1]
        for j in range(0, len(arr)):
            if i - arr[j] >= 0:
                dp[i] = max((dp[i-arr[j]] + arr[j], dp[i])) if (dp[i-arr[j]] + arr[j]) <= k else dp[i]
    print(dp)
    return dp[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for i in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)
        
        fptr.write(str(result) + '\n')
    
    fptr.close()
