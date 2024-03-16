from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# create btree (https://stackoverflow.com/a/64641132)
def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] is None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)  # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2)  # [2, 5, 12, 25, ...]
    return pNode


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        if not root:
            return None

        root.right = self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)

        match root:
            case _ if root.val < low:
                return root.right

            case _ if root.val > high:
                return root.left

        return root


# tests
lst = [1, 0, 2]
solution = Solution()
print(solution.trimBST(creatBTree(lst, 0), low=1, high=2))

lst_2 = [3, 0, 4, None, 2, None, None, 1]
solution_2 = Solution()
print(solution_2.trimBST(creatBTree(lst_2, 0), low=1, high=3))
