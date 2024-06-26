from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        target_list = []
        i, j = 0, len(matrix) - 1
        while i <= j:
            mid = (i + j) // 2
            if target < matrix[mid][0]:
                j = mid - 1

            elif matrix[mid][-1] < target:
                i = mid + 1

            else:
                target_list = matrix[mid]
                break

        else:
            return False

        left, right = 0, len(target_list) - 1
        while left <= right and target_list:
            mid = (left + right) // 2
            if left == right and target_list[left] != target:
                break

            if (
                target_list[mid] == target
                or target_list[left] == target
                or target_list[right] == target
            ):
                return True

            elif target < target_list[mid]:
                right = mid - 1

            else:
                left = mid + 1

        else:
            return False
