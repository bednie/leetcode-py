# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node: "TreeNode", target: "TreeNode", path: list):
            if not node:
                return

            this_path = path + [node]
            if node.val == target.val:
                self.paths[target] = this_path
                return

            dfs(node.left, target, this_path)
            dfs(node.right, target, this_path)

        self.paths = {}

        dfs(root, p, [])
        dfs(root, q, [])

        lca = root
        for i in range(0, min(len(self.paths[p]), len(self.paths[q]))):
            if self.paths[p][i] is self.paths[q][i]:
                lca = self.paths[p][i]

        return lca
