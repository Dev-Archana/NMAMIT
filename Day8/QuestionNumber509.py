# Question Number: 509
# Question: Fibonacci Series Numbers
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)