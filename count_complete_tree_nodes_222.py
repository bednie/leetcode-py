from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        depth_cache = {}

        def depth(node: Optional[TreeNode], right: bool) -> int:
            if not node:
                return 0
            key = (id(node), right)
            if key not in depth_cache:
                if right:
                    depth_cache[key] = 1 + depth(node.right, True)
                else:
                    depth_cache[key] = 1 + depth(node.left, False)
            return depth_cache[key]

        if not root:
            return 0

        left, right = depth(root, False), depth(root, True)

        if left == right:
            return (2**left) - 1

        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
