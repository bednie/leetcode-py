from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []

        # bfs
        queue = [root]
        next_length = 1
        temp = []
        while queue:
            length = next_length
            next_length = 0
            level_sum = 0

            while queue:
                node = queue.pop()
                level_sum += node.val
                if node.left:
                    temp.append(node.left)
                    next_length += 1
                if node.right:
                    temp.append(node.right)
                    next_length += 1

            averages.append(level_sum / length)
            queue += temp
            temp.clear()

        return averages
