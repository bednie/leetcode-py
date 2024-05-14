from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 1
        while n > 0 and m > 0:
            # take from nums2
            if nums2[n - 1] >= nums1[m - 1]:
                nums1[-i] = nums2[n - 1]
                n -= 1

            # take from nums1
            elif nums2[n - 1] < nums1[m - 1]:
                nums1[-i] = nums1[m - 1]
                m -= 1
            i += 1

        while n > 0 and m <= 0:
            # take from nums2
            nums1[-i] = nums2[n - 1]
            n -= 1
            i += 1

        while n <= 0 and m > 0:
            # take from nums1
            nums1[-i] = nums1[m - 1]
            m -= 1
            i += 1
