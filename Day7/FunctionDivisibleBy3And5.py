# Write a program to display list of numbers present in a range of (1-100) which are completely divisible by 5 and 3
def divisible(n):
    if n>100:
        return
    if (n%3==0 and n%5==0):
        print(n)
    divisible(n+1)
divisible(1)