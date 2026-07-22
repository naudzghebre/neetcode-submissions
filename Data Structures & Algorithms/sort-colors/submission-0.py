class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, 0
        for n in nums:
            if n == 0: r += 1
            elif n == 1: w += 1
            else: b += 1

        i = 0
        while r > 0:
            nums[i], r, i = 0, r - 1, i + 1
        while w > 0:
            nums[i], w, i = 1, w - 1, i + 1
        while b > 0:
            nums[i], b, i = 2, b - 1, i + 1
        