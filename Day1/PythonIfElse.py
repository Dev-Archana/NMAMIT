# Hackerrank Python If-Else Solution
# This code checks if a number is weird or not based on given conditions.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if(n%2!=0):
        print('Weird')
    else:
        if 2<=n<=5:
            print('Not Weird')
        elif  6<=n<=20:
            print('Weird')
        elif n>20:
            print('Not Weird')
            
            
            
