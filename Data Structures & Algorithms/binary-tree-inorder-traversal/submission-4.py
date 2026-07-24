# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Iterative
    # O(n) time, O(n) space
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        in_order, stack, curr = [], [], root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            in_order.append(curr.val)
            curr = curr.right
        return in_order


    # Recursoive
    # O(n) time, O(n) space
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     in_order = []
    #     def inorder(root: Optional[TreeNode]):
    #         if not root: return
    
    #         inorder(root.left)
    #         in_order.append(root.val)
    #         inorder(root.right)
    #     inorder(root)
    #     return in_order