from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(x: int, y: int, length: int) -> 'Node':
            for i in range(length): 
                for j in range(length):
                    if grid[i + x][j + y] != grid[x][y]:
                        length //= 2

                        return Node(
                            bool(grid[x][y]),
                            False, 
                            helper(x, y, length),
                            helper(x, y+length, length),
                            helper(x+length, y, length),
                            helper(x+length, y+length, length)
                            )
                            
            return Node(bool(grid[x][y]), True)

        return helper(0, 0, len(grid))
    