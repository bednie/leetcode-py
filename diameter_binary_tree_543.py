from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], d: int):
            if not node:
                return d

            left = dfs(node.left, 0)
            right = dfs(node.right, 0)

            d += 1

            self.diameter = max(self.diameter, left + right)
            
            return max(left, right) + d

        self.diameter = 0
        dfs(root, 0)
        return self.diameter
