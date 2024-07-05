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
            for i in q[::-1]:
                node = q.pop()

                if node:
                    vals.append(node.val)
                    if order == 1:
                        temp.append(node.left)
                        temp.append(node.right)
                    else:
                        temp.append(node.right)
                        temp.append(node.left)

            if vals:
                result.append(vals)

            if temp:
                q.extend(temp)

            order *= -1

        return result
