# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        queue = [root]
        while queue:
            temp = []

            for i in queue[::-1]:
                if i:
                    r.append(i.val)
                    break

            while queue:
                node = queue.pop(0)
                if node:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)

            queue.extend(temp)

        return r
