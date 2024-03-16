from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root: Optional[TreeNode], occurrences: dict):
            match root:
                case root if root is None:
                    return None

                case _:
                    if root.val in occurrences:
                        occurrences[root.val] += 1

                    else:
                        occurrences[root.val] = 1

                    # manage dict:
                    # kick out lesser occurrences
                    # equal number of occurrences
                    # are okay since we can
                    # return more than one mode
                    return helper(root.left, occurrences), helper(
                        root.right, occurrences
                    )

        occurrences = {}
        helper(root, occurrences)
        return [i for i in occurrences if occurrences[i] == max(occurrences.values())]
