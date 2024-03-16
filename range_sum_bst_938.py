from typing import Optional

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        match root:
            case None:
                return 0

            case _ if (root.val >= low) and (root.val <= high):
                return (
                    root.val
                    + self.rangeSumBST(root.left, low, high)
                    + self.rangeSumBST(root.right, low, high)
                )

            case _ if (root.val < low):
                return sum(self.rangeSumBST(root.right, low, high))

            case _ if (root.val > high):
                return sum(self.rangeSumBST(root.left, low, high))
