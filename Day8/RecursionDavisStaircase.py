# Recursion: Davis' Staircase
# Dp : dynamic Programming Intro with memo 


import math
import os
import random
import re
import sys

memo={}

def stepPerms(n):
    if n<0:
         return 0
    elif n<=1:
         return 1
    if n in memo:
         return memo[n]
    memo[n]=(stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3))
    return memo[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
