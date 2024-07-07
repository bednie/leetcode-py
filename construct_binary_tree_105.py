from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(
            root: Optional[TreeNode], preorder: List[int], inorder: List[int]
        ) -> Optional[TreeNode]:
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder.pop(0))
            root.left = helper(root, preorder, inorder[: inorder.index(root.val)])
            root.right = helper(root, preorder, inorder[inorder.index(root.val) + 1 :])
            return root

        root = None
        root = helper(root, preorder, inorder)
        return root
