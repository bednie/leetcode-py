from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def search(i, j, grid):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
                
            if grid[i][j] == "1":
                grid[i][j] = "2"

                for di, dj in self.dirs: 
                    search(i+di, j+dj, grid)


        self.dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    search(i, j, grid)

        return count
