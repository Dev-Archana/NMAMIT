# Compare the Triplets
# This script compares two triplets and returns their scores.
# It takes two lists of integers as input and outputs the scores as a tuple.
# The first list represents Alice's scores and the second list represents Bob's scores.
# The scores are calculated as the sum of the absolute differences between corresponding elements in the two lists.


import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    n=len(a)
    a_p=0
    b_p=0
    for i in range(n):
        if a[i]>b[i]:
            a_p+=1
        elif a[i]<b[i]:
            b_p+=1
        else:
            continue
    return (a_p,b_p)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
