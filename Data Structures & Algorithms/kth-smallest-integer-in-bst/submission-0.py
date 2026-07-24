# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthsmallest = 0
        def inOrder(root: Optional[TreeNode]) -> int:
            # We need to incremenet and reassign this outer variable
            # Reassigning marks it for local scope - so we need 'nonlocal' to
            # reach out into the outer scope
            nonlocal k, kthsmallest

            if not root:
                return
            # 1. Process smallest
            inOrder(root.left)

            # Process current
            k -= 1
            if k == 0: kthsmallest = root.val

            # Process largest
            inOrder(root.right)

        inOrder(root)
        return kthsmallest