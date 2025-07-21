

# Factorial Of a number :
def fact(n):
    if(n<0):
        return 
    elif(n==1 or n==0):
        return 1 
    else:
        return fact(n-1)*n
print(fact())