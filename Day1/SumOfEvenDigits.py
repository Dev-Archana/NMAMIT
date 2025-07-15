''' 
WAP to display sum of even digits present in
 a given number 
 n=1234
 o/p: 6
'''
n=1234
sum=0
while(n!=0):
    rem=n%10
    if(rem%2==0):
        sum+=rem 
    n=n//10
print(sum)