from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode], sums: list, s: str):
            if not root:
                return

            s += str(root.val)

            if not root.left and not root.right:
                sums.append(int(s))

            helper(root.right, sums, s)
            helper(root.left, sums, s)

        sums = []
        helper(root, sums, "")
        return sum(sums)
