#!/bin/python3

import math
import string
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    ans = 0
    hashtable = {}
    alphabet = string.ascii_lowercase

    for i in range(len(s)):
        for j in range(i, len(s)):
            letter_counts = [0 for _ in alphabet]
            for letter in s[i : j + 1]:
                letter_counts[ord(letter)-ord(alphabet[0])] += 1
            letter_counts = tuple(letter_counts)
            hashtable[letter_counts] = hashtable.get(letter_counts, 0) + 1
    
    for n in hashtable.values():
        ans += (n * (n - 1)) / 2
    return int(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
