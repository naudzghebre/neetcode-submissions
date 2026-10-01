# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False

    # O(n) - hashset
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     seen = set()

    #     while head:
    #         if head in seen: return True
    #         else:
    #             seen.add(head)
    #             head = head.next
    #     return False