from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            key = id(node)
            if key not in memo:
                memo[key] = 1 + depth(node.left)
            return memo[key]

        memo = {}

        if not root:
            return 0

        left, right = depth(root.left), depth(root.right)

        if left == right:
            return (2**left) + self.countNodes(root.right)

        else:
            return (2**right) + self.countNodes(root.left)