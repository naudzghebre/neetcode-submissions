class Solution:
    # Cleaner and more optimal solution
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0

        for n in nums:
            if l < 2 or n != nums[l-2]:
                nums[l] = n
                l += 1
        return l

    # def removeDuplicates(self, nums: List[int]) -> int:
    #     if len(nums) in [0, 1, 2]: return len(nums)

    #     l, r = 0, 1

    #     while r < len(nums):
    #         if nums[r] != nums[l] or (nums[r] == nums[l] and nums[r] != nums[l-1]):
    #             l += 1
    #             nums[l] = nums[r]
    #         r += 1
        
    #     return l + 1
        