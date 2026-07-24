# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    def findMax(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        curr = root
        while True:
            if curr.right: curr = curr.right
            else: return curr

    # Recursively delete + find in order replacement and re-assign rather than copy,paste,re-delete
    # O(log n)
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left: return root.right
            elif not root.right: return root.left
            else:
                minRight = self.findMin(root.right)
                minRight.left = root.left
                return root.right

        return root

    # Recursively delete + copy value for replacement
    # O(log n)    
    # def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    #     if not root:
    #         return root

    #     if key > root.val:
    #         root.right = self.deleteNode(root.right, key)
    #     elif key < root.val:
    #         root.left = self.deleteNode(root.left, key)
    #     else:
    #         if not root.left: return root.right
    #         elif not root.right: return root.left
    #         else:
    #             minRight = self.findMin(root.right)
    #             root.val = minRight.val
    #             root.right = self.deleteNode(root.right, root.val)
    #     return root
                