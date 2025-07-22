# Map and Lambda Function 
# This code demonstrates the use of map and lambda functions to apply a transformation to a list of numbers.
cube = lambda x: x**3

def fibonacci(n):
    fib=[0,1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib[:n]

        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
