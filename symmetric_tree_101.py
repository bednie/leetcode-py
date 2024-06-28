# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        deque = [root]
        while deque:
            left, right = 0, len(deque) - 1
            while left <= right:
                if deque[left] and not deque[right] or not deque[left] and deque[right]:
                    return False

                elif (
                    deque[left] and deque[right] and deque[left].val != deque[right].val
                ):
                    return False

                else:
                    left += 1
                    right -= 1

            temp = []
            while deque:
                node = deque.pop(0)
                if node:
                    temp.append(node.left)
                    temp.append(node.right)

            deque.extend(temp)

        return True
