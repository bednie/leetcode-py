from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        nodes = deque()
        while queue:
            node = queue.popleft()
            nodes.appendleft(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        max_path_sum = float("-inf")
        node_max_sum = {}

        for node in nodes:
            left_sum = max(node_max_sum.get(node.left, 0), 0)
            right_sum = max(node_max_sum.get(node.right, 0), 0)

            max_path_sum = max(max_path_sum, node.val + left_sum + right_sum)

            node_max_sum[node] = node.val + max(left_sum, right_sum)

        return max_path_sum
