from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(node: Optional[TreeNode], k: int, v: int):
            if not node:
                return

            inOrder(node.left, self.k, self.val)

            if node.val >= self.val and self.k > 0:
                self.val = node.val
                self.k -= 1

            else:
                return

            inOrder(node.right, self.k, self.val)

        self.val, self.k = 0, k
        inOrder(root, self.k, self.val)
        return self.val
