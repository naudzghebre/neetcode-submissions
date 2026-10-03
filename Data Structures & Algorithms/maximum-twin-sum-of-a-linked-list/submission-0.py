# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Naive quick solution
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        maxTwin = 0
        i, j = 0, len(nums) - 1
        while i < j:
            maxTwin = max(maxTwin, nums[i] + nums[j])
            i, j = i + 1, j - 1
        return maxTwin
        