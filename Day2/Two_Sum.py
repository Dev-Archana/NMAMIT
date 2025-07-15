# Two_Sum.py
# This script defines a function to find two indices of numbers in a list that add up to a target value.
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return (i,j)
        