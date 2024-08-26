from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(num: str, row: int, col: int) -> bool:
            intervals = ((0, 3), (3, 6), (6, 9))
            row_int, col_int = None, None
            for interval in intervals:
                if row >= interval[0] and row < interval[1]:
                    row_int = interval

                if col >= interval[0] and col < interval[1]:
                    col_int = interval

            for x in range(row_int[0], row_int[1]):
                for y in range(col_int[0], col_int[1]):
                    if board[x][y] == num:
                        return False

            for x in range(9):
                if board[row][x] == num or board[x][col] == num:
                    return False

            return True

        def backtrack(r: int, c: int) -> bool:
            if c > 8:
                return backtrack(r + 1, 0)

            if r > 8:
                return True

            if board[r][c] != ".":
                return backtrack(r, c + 1)

            for num in "123456789":
                if is_valid(num, r, c):
                    board[r][c] = num
                    if backtrack(r, c + 1):
                        return True
                    board[r][c] = "."

            return False

        backtrack(0, 0)
