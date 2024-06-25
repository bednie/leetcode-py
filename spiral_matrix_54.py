from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            # top
            if matrix:
                ans.extend(matrix.pop(0))

            # right
            if matrix:
                for i in matrix:
                    if i:
                        ans.append(i.pop())

            # bottom
            if matrix:
                ans.extend(reversed(matrix.pop()))

            # left
            if matrix:
                for i in matrix[::-1]:
                    if i:
                        ans.append(i.pop(0))

        return ans
