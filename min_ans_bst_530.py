# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inOrder(node: Optional[TreeNode], vals: list):
            if not node:
                return

            inOrder(node.left, vals)

            vals.append(node.val)

            inOrder(node.right, vals)

        vals = []

        inOrder(root, vals)

        mn, left, right = float("inf"), 0, len(vals) - 1
        while left < right:
            mn = min(
                mn, abs(vals[left] - vals[left + 1]), abs(vals[right] - vals[right - 1])
            )
            left += 1
            right -= 1

        return mn
