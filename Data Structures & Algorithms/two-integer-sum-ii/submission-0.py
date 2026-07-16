class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sums = {}

        for i, n in enumerate(numbers):
            if target - n in sums.keys():
                return [sums[target - n] + 1, i + 1]
            else:
                sums[n] = i
        return []
        