# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        in_order = []
        return self.inorderTraversalHelper(root, in_order)

    def inorderTraversalHelper(self, root: Optional[TreeNode], inOrderList: list) -> List[int]:
        if not root:
            return inOrderList
        
        self.inorderTraversalHelper(root.left, inOrderList)
        inOrderList.append(root.val)
        self.inorderTraversalHelper(root.right, inOrderList)
        return inOrderList