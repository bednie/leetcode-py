from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        map = defaultdict(set)
        unique = set()
        nums.sort()
        start, end, mid = 0, len(nums), len(nums) // 2

        for i, j in enumerate(nums):
            map[j].add(i)
            unique.add(j)

        unique = set(tuple([i for i in sorted(list(unique))]))

        for i in range(mid, end - 1):
            for j in range(i + 1, end):
                if -(nums[i] + nums[j]) in map and map[-(nums[i] + nums[j])].difference(
                    {i, j}
                ):
                    x = tuple(sorted([nums[j], nums[i], (-(nums[i] + nums[j]))]))
                    ans.add(x)
                    if not unique.difference(set(x)):
                        return list(ans)

        for i in range(mid, start, -1):
            if ans.difference(unique) == {}:
                break
            for j in range(i - 1, start - 1, -1):
                if -(nums[i] + nums[j]) in map and map[-(nums[i] + nums[j])].difference(
                    {i, j}
                ):
                    x = tuple(sorted([nums[j], nums[i], (-(nums[i] + nums[j]))]))
                    ans.add(x)
                    if not unique.difference(set(x)):
                        return list(ans)

        return list(ans)
