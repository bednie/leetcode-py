from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.iter = []
        if self.root:
            self.dfs(self.root, self.iter)

    def dfs(self, node: Optional[TreeNode], i: List[int]):
        if not node:
            return

        if node.right:
            self.dfs(node.right, i)

        i.append(node.val)

        if node.left:
            self.dfs(node.left, i)

    def next(self) -> int:
        return self.iter.pop()

    def hasNext(self) -> bool:
        return self.iter
