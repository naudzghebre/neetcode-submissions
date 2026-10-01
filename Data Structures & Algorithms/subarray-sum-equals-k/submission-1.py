class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        count, curr_sum = 0, 0
        prefix_counts = {0:1}


        for num in nums:
            curr_sum += num

            if curr_sum - k in prefix_counts:
                count += prefix_counts[curr_sum - k]

            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
        return count
        

    # O(n^2) - brute force
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     total = 0
    #     for i in range(len(nums)):
    #         running_total = nums[i]

    #         if running_total == k: total += 1

    #         for j in range(i + 1, len(nums)):
    #             running_total += nums[j]
    #             if running_total == k: total += 1
    #     return total
