class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            subsets += [sets + [num] for sets in subsets]
        return subsets

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) == 0: return []
    #     elif len(nums) == 1: return [[nums[0]]]
    #     else:
    #         temp = []
    #         for i in range(len(nums)):
    #             temp.append(nums[0:i] + nums[i:])
    #             subset = self.subsets(nums[0:i] + nums[i:])
    #             temp.append(subset)
    #         return temp

