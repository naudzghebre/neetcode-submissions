class Solution:
    # O(n) time, O(1) space - Slow/Fast pointer - treat the values as pointers
    # instead of the indices. The idea is to use Floyd's algo but equality has to 
    # be on the "actual" object (which is why since we want to find the duplicate values
    # we treat those as the pointer)
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow] # slow.next
            fast = nums[nums[fast]] # fast.next.next
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow] # slow.next
            slow2 = nums[slow2] # slow2.next
            if slow == slow2:
                return slow

    # O(n) time, O(1) space - Use existing list to mark if we seen i in [1, n] by negating it
    # def findDuplicate(self, nums: List[int]) -> int:
    #     for n in nums:
    #         if nums[abs(n) - 1] < 0:
    #             return abs(n)
    #         nums[abs(n) - 1] *= -1
    #     return 0

    # O(n) - Naive - Place in set
    # def findDuplicate(self, nums: List[int]) -> int:
    #     seen = set()
    #     for n in nums:
    #         if n in seen: return n
    #         seen.add(n)

    # O(n log n) - Naive - Sort and traverse
    # def findDuplicate(self, nums: List[int]) -> int:
    #     nums.sort()
    #     for i in range(1, len(nums)):
    #         if nums[i] == nums[i-1]: return nums[i]
    #     return 0