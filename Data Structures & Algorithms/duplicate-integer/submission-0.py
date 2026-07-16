class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_list = set()
        for n in nums:
            if n in num_list:
                return True
            num_list.add(n)
        return False
        