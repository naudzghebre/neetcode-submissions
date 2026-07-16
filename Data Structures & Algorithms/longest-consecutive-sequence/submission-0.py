class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums = sorted(set(nums))
        maxSequence = 1
        print(nums)
        for i in range(len(nums)):
            count = 1
            while i < len(nums) - 1 and nums[i+1] - nums[i] == 1:
                count += 1
                i += 1
            maxSequence = max(maxSequence, count)
        return maxSequence

        