from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def search(i: int, j: int, board: List[List[str]]):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            if board[i][j] == "O":
                board[i][j] = "o"
                self.regions[self.count].append((i, j))
                for di, dj in self.dirs:
                    search(i + di, j + dj, board)

        def border(coord: tuple, direction: tuple):
            i, j = coord
            di, dj = direction

            # a cell "inherits" the surroundedness of
            # its neighbor in that direction
            if coord in self.memo:
                return self.memo[coord]

            # reached border without finding an 'X'
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                self.memo[coord] = False
                return False

            # found an 'O', keep going in same direction
            if board[i][j] == "o":
                return border((i + di, j + dj), direction)

            # bordered by 'X'
            if board[i][j] == "X":
                self.memo[coord] = True
                return True

        self.dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        self.regions = {}
        self.surrounded = {}
        self.memo = {}
        self.count = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    self.regions[self.count] = []
                    self.surrounded[self.count] = []
                    search(i, j, board)
                    self.count += 1

        for r in range(self.count):
            for c in self.regions[r]:
                if (
                    border(c, self.dirs[0])
                    and border(c, self.dirs[1])
                    and border(c, self.dirs[2])
                    and border(c, self.dirs[3])
                ):
                    self.surrounded[r].append(c)

            if self.regions[r] == self.surrounded[r]:
                for i, j in self.regions[r]:
                    board[i][j] = "X"
            else:
                for i, j in self.regions[r]:
                    board[i][j] = "O"
