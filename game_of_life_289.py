from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        prev = copy.deepcopy(board)
        m = len(prev)
        n = len(prev[0])
        neighbors = (
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
        )

        # count neighbors & apply rules
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for neighbor in neighbors:
                    if 0 <= i + neighbor[0] < m and 0 <= j + neighbor[1] < n:
                        live_neighbors += prev[i + neighbor[0]][j + neighbor[1]]

                p = prev[i][j]
                if live_neighbors < 2 and p == 1:
                    board[i][j] = 0
                elif (live_neighbors == 2 or live_neighbors == 3) and p == 1:
                    board[i][j] = 1
                elif live_neighbors == 3 and p == 0:
                    board[i][j] = 1
                elif live_neighbors > 3 and p == 1:
                    board[i][j] = 0
