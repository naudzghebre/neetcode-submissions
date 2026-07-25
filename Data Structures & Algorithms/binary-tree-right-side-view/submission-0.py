# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue , rightView = deque(), []

        if root: queue.append(root)

        while len(queue) > 0:
            rightSide = None
            lenLevel = len(queue)
            for i in range(lenLevel):
                node = queue.popleft()
                rightSide = node

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            rightView.append(rightSide.val)
        return rightView

            


        