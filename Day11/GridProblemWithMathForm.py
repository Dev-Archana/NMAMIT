# Mathematical Approach (Combinatorics)
import math

def grid_traveler(m, n):
    return math.comb(m + n - 2, m - 1)
print(grid_traveler(2, 3))  