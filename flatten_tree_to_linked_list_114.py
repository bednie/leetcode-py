from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preOrder(node: Optional[TreeNode]):
            if not node:
                return

            self.nodes.append(node)

            preOrder(node.left)
            preOrder(node.right)

        self.nodes = []
        preOrder(root)

        if not self.nodes:
            return root

        self.nodes[0].left = None
        head = self.nodes[0]

        for node in self.nodes[1:]:
            head.left = None
            head.right = node
            head = node

        return root
