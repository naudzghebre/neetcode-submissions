# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = list(lists) # O(k)
        head = tail = ListNode()

        # O(n)
        while True:
            # O(k)
            candidates = [(i, node) for i, node in enumerate(heads) if node]
            if not candidates:
                break

            # O(k)
            min_ind, min_node = min(candidates, key=lambda pair: pair[1].val)

            heads[min_ind] = min_node.next
            tail.next = min_node
            tail = min_node
        tail.next = None
        return head.next

        