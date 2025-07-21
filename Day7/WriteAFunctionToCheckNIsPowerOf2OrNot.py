'''
Program to check and return true if a user-given number is the power 
of 2,else return false.
'''

def powcheck(n):
    while(n>1):
        if(n%2==0):
            n = n//2
        else:
            return False
    return True
def main():
    n = 16
    print(powcheck(n))
main()