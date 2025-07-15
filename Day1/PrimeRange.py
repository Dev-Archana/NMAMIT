# Write a program to display list of prime numbers present in the range of 1-10
# n=10
# for i in range(2,n+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#             print(i)

num = 14
isprime = True

def primeno(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

for i in range(2, num):
    if primeno(i):
        print(i)
        
