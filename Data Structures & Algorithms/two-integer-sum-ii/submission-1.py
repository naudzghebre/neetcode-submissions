class Solution:

    # [-2, 1, 3, 4, 5, 6, 10] target = 9
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


    # This is good, but there's better with O(1) space
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     sums = {}

    #     for i, n in enumerate(numbers):
    #         if target - n in sums.keys():
    #             return [sums[target - n] + 1, i + 1]
    #         else:
    #             sums[n] = i
    #     return []
        