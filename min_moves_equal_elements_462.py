# leetcode 462: minimum moves to equal array elements ii
# Blair Ednie

from typing import List
from math import ceil
from statistics import median


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # find the median of nums
        target = ceil(median(nums))

        # distance from median for each value in nums
        min_moves = 0
        for i in nums:
            min_moves += abs(target - i)

        return min_moves


solution = Solution()
test1 = [1, 2, 3]
test2 = [1, 10, 2, 9]
print(solution.minMoves2(test1))
print(solution.minMoves2(test2))
