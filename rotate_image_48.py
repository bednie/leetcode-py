from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        for i in matrix:
            i.reverse()

        start = length - 1
        end = 0
        while start > 0:
            for i in range(start + 1):
                matrix[start - i][end], matrix[start][end + i] = (
                    matrix[start][end + i],
                    matrix[start - i][end],
                )
            start -= 1
            end += 1

        return
