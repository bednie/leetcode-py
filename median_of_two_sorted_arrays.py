# 4. Median of Two Sorted Arrays 
import heapq
import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if not nums1 and not nums2:
            return 0
        
        median = 0.0
        merged = []

        for i in heapq.merge(nums1,nums2):
            merged.append(i)

        length = len(merged)
        if length % 2 == 0:
            low = math.floor(length / 2 - 1 ) # low index
            high = math.ceil(length / 2 )     # high index
            median = (merged[low] + merged[high]) / 2
        else:
            median = merged[int(length / 2)]
        return median