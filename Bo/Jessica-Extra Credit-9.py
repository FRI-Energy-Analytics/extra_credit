#!/bin/python3

import math
import os
import random
import re
import sys

def putCrosses(board):
    list = []
    for i in range(1,len(board)-1):
        for j in range(1, len(board)-1):
            value = board[i][j]
            if (board[i][j-1] < value) and (board[i][j+1] < value) and (board[i+1][j] < value) and (board[i-1][j] < value):
                    list.append((i,j))
    for (a,b) in list:
        board[a][b] = "X"
    return board
    
def printSquare(sA):
    for array in sA:
        printArray(array)

def printArray(array):
    output = ""
    for a in array:
        output += str(a)
    print(output)

sizeOfInput = int(input())

board = []
for i in range(sizeOfInput):
    row = input()
    board.append([])
    for r in row:
        board[i].append(int(r))
crossed = putCrosses(board)
printSquare(crossed)