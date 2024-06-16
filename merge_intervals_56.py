from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] < intervals[i + 1][0]:
                i += 1

            else:
                r = sum([intervals[i], intervals.pop(i + 1)], [])
                intervals[i] = [min(r), max(r)]

        return intervals
