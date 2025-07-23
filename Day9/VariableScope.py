# global scoped :
x=7
def display1():
    global x
    x=3
    print(x)
display1()