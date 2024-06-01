from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1 
        reachable = [0]
        seen = set()

        if 0 not in nums and end > 1:
            return True

        while reachable:
            idx = reachable.pop()
            if idx >= end:
                return True
            if nums[idx] != 0:
                seen.add(idx)
                reachable += [i for i in range(idx+1, idx+nums[idx]+1) if i not in seen]
        return False