class Solution:
    # O(n) - Naive - Place in set
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen: return n
            seen.add(n)