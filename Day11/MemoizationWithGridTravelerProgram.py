#  Memoization (Top-Down DP)
def grid_traveler1(m, n, memo=None):
     if memo is None:
         memo = {}
     key = (m, n)
     if key in memo:
         return memo[key]
     if m == 1 and n == 1:
         return 1
     if m == 0 or n == 0:
         return 0
     memo[key] = grid_traveler1(m - 1, n, memo) + grid_traveler1(m, n - 1, memo)
     return memo[key]

