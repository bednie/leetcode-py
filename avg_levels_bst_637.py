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
        while queue:
            length = len(queue)
            temp = []
            level_sum = 0

            while queue:
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            averages.append(level_sum / length)
            queue += temp

        return averages
