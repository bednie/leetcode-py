from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        def dfs(node: Optional["Node"], seen: set) -> Optional["Node"]:
            if not node:
                return None

            if node in seen:
                return seen[node]

            new = Node(node.val)
            self.seen[node] = new
            for n in node.neighbors:
                new.neighbors.append(dfs(n, self.seen))

            return new

        self.seen = {}
        return dfs(node, self.seen)
