import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input() #takes in string

    letters = {}
    for i in range(len(s)): # iterates through input string
        if s[i] in letters:
            #key value pair: key = letter in word, value = array of letter in word and count
            letters[s[i]] = [s[i], letters[s[i]][1] + 1] 
        else:
            letters[s[i]] = [s[i], 1]
    #sorts the dictionary in descending order based on descending order of second value in arrays and then ascdending order of first values of arrays (technically key)
    sorted_letters = sorted(letters.values(), key=lambda x:(-x[1],x[0]))

    print('\n'.join(list(map(lambda x: x[0]+ " " +str(x[1]), sorted_letters[:3]))))
