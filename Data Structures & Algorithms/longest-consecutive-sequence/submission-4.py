class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        numSet = set(nums)
        maxSequence = 1
        for i in range(len(nums)):
            if nums[i] - 1 in numSet:
                continue
            else:
                count = 1
                n = nums[i]
                while n+1 in numSet:
                    count += 1
                    n += 1
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

        