from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals

        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        result = []
        i, j = 0, len(intervals) - 1
        while i <= j:
            if intervals[i][1] < newInterval[0]:
                i += 1
            else:
                break

        while j >= 0:
            if intervals[j][0] > newInterval[1]:
                j -= 1
            else: 
                break

        if i <= j:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[j][1], newInterval[1])]

        # build result
        result.extend(intervals[0:i])
        result.append(newInterval)
        result.extend(intervals[j+1:])
        return result
