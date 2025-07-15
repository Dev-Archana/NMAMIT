# Hackerrank Python Challenge
# Task: Print numbers from 1 to n without spaces or newlines in between.
# PrintFunction.py
# This script prints numbers from 1 to n without spaces or newlines in between.
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')
