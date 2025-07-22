class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels) # Convert to set for fast lookup
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count