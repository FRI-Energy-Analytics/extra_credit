#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):

    top = n - r_q
    bottom = r_q - 1
    right = n - c_q
    left = c_q - 1

    top_left = min(n - r_q, c_q - 1)
    top_right = n - max(c_q, r_q)
    bottom_left = min(r_q, c_q) - 1
    bottom_right = min(r_q - 1, n - c_q)

    for i in range(k):
        obstacle_row, obstacle_column = obstacles[i][0], obstacles[i][1]
        
        if obstacle_row == r_q:
            if obstacle_column > c_q:
                top = min(top, obstacle_column - c_q - 1)
            else:
                bottom = min(bottom, c_q - obstacle_column - 1)

        elif obstacle_column == c_q:
            if obstacle_row > r_q:
                right = min(right, obstacle_row - r_q - 1)
            else:
                left = min(left, r_q - obstacle_row - 1)
        
        elif abs(obstacle_column - c_q) == abs(obstacle_row - r_q):
            
            if obstacle_column > c_q and obstacle_row > r_q:
                top_right = min(top_right, obstacle_column - c_q - 1)
            
            elif obstacle_column > c_q and obstacle_row < r_q:
                bottom_right = min(bottom_right, obstacle_column - c_q - 1)
            
            elif obstacle_column < c_q and obstacle_row > r_q:
                top_left = min(top_left, c_q - obstacle_column - 1)
            
            elif obstacle_column < c_q and obstacle_row < r_q:
                bottom_left = min(bottom_left, c_q - obstacle_column - 1)
                
    return top + bottom + right + left + top_left + top_right + bottom_left + bottom_right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
