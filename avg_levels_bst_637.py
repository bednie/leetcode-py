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
            # average for this level
            level_sum = 0
            for node in queue:
                level_sum += node.val
            averages.append(level_sum / len(queue))

            # get next level
            temp = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue += temp

        return averages
