# 5. LeetCode 1122
# Please finish LeetCode 1122. Relative Sort Array
# (https://leetcode.com/problems/relative-sort-array/description/).
# 1. You are NOT allowed to use built-in functional APIs of your chosen programming lan- guage. Feel free to implement some inefficient sorting algorithm (e.g., O(n2) sorting algorithms). You won’t get the “Time Limit Exceeded” error in this problem.
# 2. You will obtain a bonus of up to 10 points if you could implement a solution that takes O(1) extra space.
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """create a state machine where:
        state A: sort arr1 in-place relative to arr2. Once arr2 is exhausted, move to state B.
        state B: sort remaining elements in ascending order then return original arr1 which
        is now sorted relative to arr2"""

        # swap in-place
        # use O(1) space by swapping elements one at a time, in-place
        def swap_values(arr: List[int], index1: int, index2: int):
            arr[index1], arr[index2] = arr[index2], arr[index1]

        # state A
        sorted_index = 0
        for i in range(len(arr2)):
            for j in range(sorted_index, len(arr1)):
                if arr1[j] == arr2[i]:
                    swap_values(arr1, j, sorted_index)
                    sorted_index += 1

        # state B
        for i in range(sorted_index, len(arr1)):
            min_index = i
            for j in range(i + 1, len(arr1)):
                if arr1[j] < arr1[min_index]:
                    min_index = j
            swap_values(arr1, i, min_index)

        return arr1


solution = Solution()
sol1 = solution.relativeSortArray(
    [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]
)
print(sol1)
assert sol1 == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19], "wrong"
print(solution.relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))

sol2 = solution.relativeSortArray([26, 21, 11, 20, 50, 34, 1, 18], [21, 11, 26, 20])
print(sol2)

sol3 = solution.relativeSortArray(
    [33, 22, 48, 4, 39, 36, 41, 47, 15, 45], [22, 33, 48, 4]
)
print(sol3)
