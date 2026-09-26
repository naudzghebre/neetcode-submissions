class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total, windowSize = 0, 0, len(nums) + 1

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                windowSize = min(windowSize, R - L + 1)
                total -= nums[L]
                L += 1

        return 0 if windowSize == len(nums) + 1 else windowSize
