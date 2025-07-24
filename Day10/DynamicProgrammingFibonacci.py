# Memo With Fibonacci 
def fibonacci(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo)
    return memo[n]
print(fibonacci(15))

# fib(1)+fib(0)
#  ||
# fib(2)+fib(1) fib(1)+fib(0) 
#      ||         ||
#     fib(3)+fib(2)   fib(1)+fib(0) 
#           ||            ||      
# fib(5)=>fib(4)+fib(3)=>fib(2)+fib(1)
#           ||
#     fib(3)+fib(2)
#       ||        ||
# fib(2)+fib(1)   fib(1)+fib(0)
#   ||
# fib(0)+fib(1)