# built to run on python 3
import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
sto = ""
flip = False

for i in range(n):
    matrix_item = input()
    matrix.append(list(matrix_item))

for col in range(m):
    for row in range(n):
        sto += matrix[row][col]
stoSaver = sto
sto = re.sub("(?<=[\w|\d])+(!|@|#|\$|%|&|\s)+(?=[\w|\d])+"," ",sto)
print(sto)
