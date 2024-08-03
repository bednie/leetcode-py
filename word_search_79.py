from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(word: str, seen: list):
            if not word:
                self.result = True
                return

            i,j = seen[-1]

            n = (i-1,j) if i-1 >= 0 else None
            s = (i+1,j) if i+1 < self.m else None
            e = (i,j+1) if j+1 < self.n else None
            w = (i,j-1) if j-1 >= 0 else None

            for c in [n,s,e,w]:
                if c and self.board[c[0]][c[1]] == word[0] and c not in seen:
                    s = seen + [c]
                    dfs(word[1:], s)

            return

        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.result = False
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == word[0]:
                    dfs(word[1:], [(i,j)])

        return self.result