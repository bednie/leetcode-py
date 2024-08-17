from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def unravel(board: List[List[int]]) -> List[int]:
            b = [0]
            n = len(board)
            for i in range(len(board) - 1, -1, -1):
                if (n - i) % 2 == 1:
                    b += board[i]
                else:
                    b += reversed(board[i])

            return b

        board = unravel(board)
        dq = [(1, 0)]
        visited = set()

        while dq:
            pos, moves = dq.pop(0)

            for i in range(1, 7):
                next_pos = pos + i

                if next_pos > len(board) - 1:
                    break

                if board[next_pos] != -1:
                    next_pos = board[next_pos]

                if next_pos == len(board) - 1:
                    return moves + 1

                if next_pos not in visited:
                    visited.add(next_pos)
                    dq.append((next_pos, moves + 1))

        return -1
