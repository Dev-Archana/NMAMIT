def printNumber(n):
    if(n<=10):
        if(n%2==0):
            print(n)
        printNumber(n+1)
printNumber(1)