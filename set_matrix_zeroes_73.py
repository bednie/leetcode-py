import copy
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = copy.deepcopy(matrix)
        cols = []

        for i, j in enumerate(temp):
            for k in range(len(j)):
                if j[k] == 0:
                    cols.append(k)
                    matrix[i] = [0] * len(j)

        for i in cols:
            for j in matrix:
                j[i] = 0
