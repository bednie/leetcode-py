from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {-1: 1}
        for i in range(0, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]

        suffix = {len(nums): 1}
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]

        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefix[i - 1] * suffix[i + 1]

        return ans
