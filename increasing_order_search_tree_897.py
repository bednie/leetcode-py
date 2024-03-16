# Given the root of a binary search tree,
# rearrange the tree in in-order so that
# the leftmost node in the tree is now the
# root of the tree, and every node has no left
# child and only one right child.i

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# in-order, recursive solution
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = TreeNode()
        self.tail = head

        def helper(node: TreeNode):
            match node:
                case None:
                    return None

                case _:
                    helper(node.left)
                    node.left = None  # tree is right-skewed
                    self.tail.right = node  # attach node to tail.right
                    self.tail = self.tail.right  # update tail
                    helper(node.right)

        helper(root)  # inital recursive call
        return head.right  # head is a dummy node, so return head.right
