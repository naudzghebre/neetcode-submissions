class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        to_insert = TreeNode(key, val)

        if not self.root:
            self.root = to_insert
            return

        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = to_insert
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = to_insert
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key == curr.key:
                return curr.val
            elif key < curr.key: curr = curr.left
            else: curr = curr.right
        return -1


    def getMin(self) -> int:
        curr = self._findMin(self.root)
        return curr.val if curr else -1


    def getMax(self) -> int:
        maxVal = -1
        curr = self.root
        while curr:
            maxVal = curr.val
            curr = curr.right
        return maxVal

    def _findMin(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def _remove(self, key: int, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        if key > root.key:
            root.right = self._remove(key, root.right)
        elif key < root.key:
            root.left = self._remove(key, root.left)
        else:
            if not root.left: return root.right
            elif not root.right: return root.left
            else:
                # 1. Find the MIN of the right subtree of the chosen node
                # 2. Assign to that min node's left^ the values of the chosen's node's lef tsubtree
                # 3. Return the right subtree, since the left subtree was effectively copied over to the bottom
                # of the the right subtree.
                minRight = self._findMin(root.right)
                minRight.left = root.left
                return root.right
        return root

    def remove(self, key: int) -> None:
        self.root = self._remove(key, self.root)

    def _inOrderTraversal(self, root: TreeNode, result: List[int]):
        if root != None:
            self._inOrderTraversal(root.left, result)
            result.append(root.key)
            self._inOrderTraversal(root.right, result)

    def getInorderKeys(self) -> List[int]:
        result = []
        self._inOrderTraversal(self.root, result)
        return result

