def Factorial(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return 1
    memo[n]=n*Factorial(n-1) 
    return memo[n]
print(Factorial(5))