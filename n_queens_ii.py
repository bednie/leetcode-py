class Solution:
    def totalNQueens(self, n: int) -> int:
        def isSafe(i: int, j: int) -> bool:
            if i in self.rows:
                return False

            for d in range(1, n + 1):
                if (
                    (i + d, j + d) in self.positions
                    or (i + d, j - d) in self.positions
                    or (i - d, j + d) in self.positions
                    or (i - d, j - d) in self.positions
                ):
                    return False

            return True

        def backtrack(row: int, col: int):
            # positions in this col are exhausted
            if col > n - 1:
                return

            # backtrack
            for r in range(n):
                if isSafe(r, col):
                    self.positions[(r, col)] = True
                    self.rows[r] = True

                    if len(self.positions) == n:
                        self.solutions += 1

                    backtrack(0, col + 1)

                    self.positions.pop((r, col))
                    self.rows.pop(r)

        # create and set up board
        if n == 1:
            return 1

        if n <= 3:
            return 0

        self.positions = {}
        self.rows = {}
        self.solutions = 0

        # new board
        for start in range(n):
            self.positions[(start, 0)] = True
            self.rows[start] = True
            backtrack(0, 1)
            self.positions.clear()
            self.rows.clear()

        return self.solutions
