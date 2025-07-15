# Leetcode challenge

class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
# This function calculates the digital root of a number.
# The digital root is the single-digit value obtained by an iterative process of summing digits.
# The function takes an integer as input and returns the digital root of that number.