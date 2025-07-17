# Input -> s=a1b1
# Output -> [a1b1,A1b1,a1B1,A1B1]
class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = [""]
        for char in s:
            if char.isalpha():
                res = [prefix + char.lower() for prefix in res] + [prefix + char.upper() for prefix in res]
            else:
                res = [prefix + char for prefix in res]
        return res


sol = Solution()
print(sol.letterCasePermutation('a1b1'))