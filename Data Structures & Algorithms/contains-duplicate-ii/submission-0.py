class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = {}

        for i, n in enumerate(nums):
            if n in window and abs(i - window[n]) <= k:
                return True
            else:
                window[n] = i
        return False