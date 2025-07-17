class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and convert to lowercase
        clean_s = ''.join(c.lower() for c in s if c.isalnum())
        
        # Compare the cleaned string with its reverse
        return clean_s == clean_s[::-1]
sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(sol.isPalindrome("race a car"))                      # False
print(sol.isPalindrome(" "))                               # True
