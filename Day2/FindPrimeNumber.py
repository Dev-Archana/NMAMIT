# FindPrimeNumber.py
# This script defines a function to check if a number is prime.
# It then checks a list of numbers and prints the prime numbers.

def isprime(n):
    if n==2:
        return True
    else:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                return False
        return True
a=[2,3,4,5,36,27,47]
for i in range(len(a)):
    if isprime(a[i]):
        print(a[i])