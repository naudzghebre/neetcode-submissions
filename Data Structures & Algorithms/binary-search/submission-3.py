class Solution:

    def search(self, nums: List[int], target: int) -> int:
        return self.searchBinary(nums, target, 0, len(nums) - 1)

    def searchBinary(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left >= right:
            return left if nums[left] == target else -1

        m = (left + right) // 2

        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.searchBinary(nums, target, m + 1, right)
        else:
            return self.searchBinary(nums, target, left, m - 1)

    # def search(self, nums: List[int], target: int) -> int:
    #     n, l, r = len(nums), 0, len(nums) - 1

    #     while l <= r:
    #         m = (l+r) // 2

    #         if nums[m] == target: return m
    #         elif nums[m] < target: l = m + 1
    #         else: r = m - 1
    #     return -1


        