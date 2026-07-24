# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        nodeInd = {}
        for i, n in enumerate(inorder):
            nodeInd[n] = i

        i = 0
        root = None
        def buildSubtree(l: int, r: int) ->  Optional[TreeNode]:
            nonlocal i, preorder, nodeInd

            if l == r:
                return None
            else:
                node = TreeNode(val=preorder[i])
                inorderInd = nodeInd[preorder[i]]

                # print("i: " + str(i) + " left: " + str(inorder[l:inorderInd]))
                # print("i: " + str(i) + " right: " + str(inorder[inorderInd + 1:r]))

                i += 1
                node.left = buildSubtree(l, inorderInd)
                node.right = buildSubtree(inorderInd + 1, r)

                return node

        root = buildSubtree(0, len(inorder))
        return root

        


        
        