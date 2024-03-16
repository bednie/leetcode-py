from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        first_unsorted_index = None
        last_unsorted_index = None

        # first unsorted
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                first_unsorted_index = i
                break

        if first_unsorted_index is None:
            return 0  # list is non-decreasing (i.e., sorted)

        # last unsorted
        for i in range(len(nums) - 1, first_unsorted_index, -1):
            if nums[i] < nums[i - 1]:
                last_unsorted_index = i
                break

        # get min and max unsorted elements in the unsorted range
        max_unsorted = -100_001
        min_unsorted = 100_001
        for i in nums[first_unsorted_index : last_unsorted_index + 1]:
            # update min and max unsorted
            if i < min_unsorted:
                min_unsorted = i
            if i > max_unsorted:
                max_unsorted = i

        # for min_unsorted, find last element that min_unsorted is greater than
        for i in range(0, len(nums) - 1):
            if min_unsorted < nums[i]:
                # update first unsorted index if i is smaller
                first_unsorted_index = min(i, first_unsorted_index)

        # for max_unsorted, find last element that max_unsorted is less than
        for i in range(len(nums) - 1, -1, -1):
            if max_unsorted > nums[i]:
                # update last unsorted index if i is smaller
                last_unsorted_index = max(i, last_unsorted_index)

        return last_unsorted_index - first_unsorted_index + 1


# testcases
solution = Solution()
print(solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(solution.findUnsortedSubarray([1, 2, 3, 4]))
print(solution.findUnsortedSubarray([2, 3, 3, 2, 4]))
print(solution.findUnsortedSubarray([1, 3, 2, 2, 2]))
print(solution.findUnsortedSubarray([1, 2, 5, 3, 4]))
