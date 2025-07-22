def fibonacci(n):
    if n<0:
        return "Not defined"
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:   
        return fibonacci(n-1)+fibonacci(n-2)
    
s=int(input("Enter a number:"))
print(fibonacci(s))
    