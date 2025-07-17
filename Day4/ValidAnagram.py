from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
# Leet Code Problem: Valid Anagram
# This code checks if two strings are anagrams of each other using the Counter class from the
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  # True
print(sol.isAnagram("rat", "car"))          # False

