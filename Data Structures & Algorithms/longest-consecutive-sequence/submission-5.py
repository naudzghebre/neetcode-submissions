class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSequence = 0
        for n in nums:
            if n - 1 not in numSet:
                count = 0
                while n + count in numSet:
                    count += 1
                maxSequence = max(maxSequence, count)
        return maxSequence

    
    # Big O of this is nlogn because of the sorting, question asks for O(n)
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums) <= 1:
    #         return len(nums)

    #     nums = sorted(set(nums))
    #     maxSequence = 1
    #     print(nums)
    #     for i in range(len(nums)):
    #         count = 1
    #         while i < len(nums) - 1 and nums[i+1] - nums[i] == 1:
    #             count += 1
    #             i += 1
    #         maxSequence = max(maxSequence, count)
    #     return maxSequence

        