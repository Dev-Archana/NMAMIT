# Write_a_function.py
# This script defines a function to check if a year is a leap year.
# A year is a leap year if it is divisible by 4, but not divisible by 100, unless it is also divisible by 400.

def is_leap(year):
    leap = False
    
    if(year%4==0 and year%100!=0 or year%400==0):
        leap=True
    
    return leap

year = int(input())
print(is_leap(year))