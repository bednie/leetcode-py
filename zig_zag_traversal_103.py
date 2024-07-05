from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = [root]
        order = 1

        while q:
            temp = []
            vals = []
            for i in q[::order]:
                if order == 1:
                    node = q.pop(0)
                    if node:
                        vals.append(node.val)

                elif order == -1:
                    node = q.pop()
                    if node:
                        vals.append(node.val)

                if node:
                    temp.append(node.left)
                    temp.append(node.right)

            order *= -1
            if vals:
                result.append(vals)
            if temp:
                q.extend(temp)

        return result
