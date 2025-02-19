from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        idx = 0

        while idx < len(seats):
            start = idx
            if seats[idx] == 0:
                while idx < len(seats) and seats[idx] == 0:
                    idx += 1

                if start == 0 or idx == len(seats):
                    max_distance = max(max_distance, idx - start)
                else:
                    max_distance = max(max_distance, (idx - start + 1) // 2)
               
            idx += 1

        return max_distance

# test
sol = Solution()
assert sol.maxDistToClosest([1,0,0,0,1,0,1]) == 2