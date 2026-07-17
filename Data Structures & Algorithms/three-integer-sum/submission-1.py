class Solution:

    # nums=[-1,0,1,2,-1,-4]
    # [-4, -1, -1, 0, 1, 2]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == n:
                continue
            
            j, k = i+1, len(nums) - 1
            while j < k:
                three_sum = n + nums[j] + nums[k]
                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return res

    # Doesn't work
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums = sorted(nums)

    #     sums = {}
    #     triplets = []
    #     for i in range(len(nums) - 1):
    #         for j in range(i + 1, len(nums)):
    #             sums.setdefault(0 - nums[i] - nums[j], set()).add(tuple(sorted((nums[i], nums[j]))))

    #     for k in range(len(nums)):
    #         if 0 - nums[k] in sums.keys():
    #             tuples = sums[0 - nums[k]]
    #             for t in tuples:
    #                 triplets.append([nums[k], t[0], t[1]])

    #     print(sums)
    #     return triplets