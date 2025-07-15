'''
WAP to print sum of digits present in a given 
number 
n=1234
o/p: 10
'''
n=1234
sum=0
while(n!=0):
    rem=n%10
    sum+=rem
    n=n//10
print(sum)
