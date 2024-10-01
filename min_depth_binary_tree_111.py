from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode], depth: int):
            if not root or depth > self.result:
                return

            if not root.left and not root.right:
                self.result = min(self.result, depth + 1)
                return

            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
            return

        self.result = 10_000 if root else 0
        helper(root, 0)
        return self.result
