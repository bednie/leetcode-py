from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        map = defaultdict(set)
        nums.sort()

        for i, j in enumerate(nums):
            map[j].add(i)

        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] + nums[i] > 0:
                    end -= 1
                elif nums[start] + nums[end] + nums[i] < 0:
                    start += 1
                else:
                    if -(nums[start] + nums[end]) in map and (
                        i != start and i != end and start != end
                    ):
                        ans.add(tuple([nums[start], nums[end], nums[i]]))
                    start += 1
                    end -= 1

        return list(ans)
