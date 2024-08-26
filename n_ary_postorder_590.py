from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        def helper(node: "Node") -> List[int]:
            if not node:
                return

            for child in node.children:
                helper(child)

            self.postorder.append(node.val)

        self.postorder = []
        helper(root)
        return self.postorder
