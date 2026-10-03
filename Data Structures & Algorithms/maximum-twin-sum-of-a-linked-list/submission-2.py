# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) time, O(1) space - Reverse first half
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        maxTwin = 0
        while slow:
            maxTwin = max(maxTwin, slow.val + prev.val)
            prev, slow = prev.next, slow.next
        return maxTwin

    # O(n) time, O(n) space - One pass
    # def pairSum(self, head: Optional[ListNode]) -> int:
    #     slow = fast = head
    #     nums = []
    #     while fast and fast.next:
    #         nums.append(slow.val)
    #         slow, fast = slow.next, fast.next.next
        
    #     maxTwin = 0
    #     for i in range(len(nums) - 1, -1, -1):
    #         maxTwin = max(maxTwin, slow.val + nums[i])
    #         slow = slow.next
    #     return maxTwin

    # O(n) time, O(n) space - Naive brute force solution
    # def pairSum(self, head: Optional[ListNode]) -> int:
    #     nums = []
    #     while head:
    #         nums.append(head.val)
    #         head = head.next
        
    #     maxTwin = 0
    #     i, j = 0, len(nums) - 1
    #     while i < j:
    #         maxTwin = max(maxTwin, nums[i] + nums[j])
    #         i, j = i + 1, j - 1
    #     return maxTwin
        