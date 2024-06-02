from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [float('inf') for i in range(len(nums))]
        memo[0] = 0
        for i,j in enumerate(nums):
            for k in range(i+1, min(i+j+1, len(nums))):
                memo[k] = min(memo[k], memo[i]+1)
        return memo[-1]