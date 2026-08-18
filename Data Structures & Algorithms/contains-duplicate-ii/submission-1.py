class Solution:

    # HashSet
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False

    # HashMap
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     window = {}

    #     for i, n in enumerate(nums):
    #         if n in window and abs(i - window[n]) <= k:
    #             return True
    #         else:
    #             window[n] = i
    #     return False