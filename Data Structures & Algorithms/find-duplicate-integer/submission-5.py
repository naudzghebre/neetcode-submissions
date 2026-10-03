class Solution:

    # def findDuplicate(self, nums: List[int]) -> int:
    #     if nums[0] == nums[1]: return nums[0]
    #     elif nums[0] == nums[2] or nums[1] == nums[2]: return nums[2]

    #     slow, fast = 0, 0

    #     while slow < len(nums):
    #         slow, fast = slow + 1, fast + 2
    #         print("slow: ", nums[slow], "fast: ", nums[fast])
    #         if nums[slow] == nums[fast]:
    #             print("slow", slow)
    #             break
    #     print("intersect", slow)
        
    #     return nums[slow]

    # O(n) - Naive - Place in set
    # def findDuplicate(self, nums: List[int]) -> int:
    #     seen = set()
    #     for n in nums:
    #         if n in seen: return n
    #         seen.add(n)

    # O(n log n) - Naive - Sort and traverse
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: return nums[i]
        return 0