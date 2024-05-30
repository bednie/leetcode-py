from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] + nums[i] > 0:
                    end -= 1
                elif nums[start] + nums[end] + nums[i] < 0:
                    start += 1
                else:
                    if i != start and i != end:
                        ans.add((nums[start], nums[end], nums[i]))

                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1

        return ans
