from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) / 2
        d = {}
        max_seen = (0, 0)
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1 

            if d[i] > max_seen[1]:
                max_seen = (i, d[i])
            
            if max_seen[1] > majority:
                return i
        
        return max_seen[0]
