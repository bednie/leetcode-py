from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] < intervals[i+1][0]:
                result.append(intervals[i])
                i += 1

            else:
                r = sum([intervals[i], intervals.pop(i+1)], [])
                print(r)
                intervals[i] = [min(r), max(r)]

        result.extend(intervals[i:])
        return result
