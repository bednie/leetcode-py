from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1

        while i < j:
            mid = (j + i) // 2

            if nums[mid - 1] <= nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] <= nums[mid + 1]:
                i = mid + 1
            else:
                j = mid
        return i
