from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = []
        for p in points:
            if not arrows:
                arrows.append(p)
                continue

            if p[0] <= arrows[-1][1]:
                arrows[-1][0] = max(arrows[-1][0], p[0])
                arrows[-1][1] = min(arrows[-1][1], p[1])
            else:
                arrows.append(p)

        return len(arrows)