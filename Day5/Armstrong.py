
n = 153
temp = n
d = 0


while(temp != 0):
    temp = temp // 10
    d += 1


temp = n
sum = 0
while(temp != 0):
    rem = temp % 10
    sum += rem ** d
    temp = temp // 10


if sum == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
