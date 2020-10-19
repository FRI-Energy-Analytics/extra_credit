#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    s1_s3=Counter(s1)
    s2_s3=Counter(s2)
    deletecount=0
    for i in s1_s3.keys():
        deletecount += abs(s1_s3[i]-s2_s3[i])
        del s2_s3[i]
    
    deletecount += sum(s2_s3.values())  
    return deletecount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
