import itertools
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        lines = {}  # (float("inf"), x) or (0, y) or (slope, y_int)
        max_points = 0
        pairs = itertools.combinations(points, 2)

        for i in pairs:
            rise = i[1][1] - i[0][1]
            run = i[1][0] - i[0][0]
            if run != 0:
                slope = rise / run
            else:
                slope = float("inf")

            y_int = i[1][1] - (slope * i[1][0])

            if (slope, i[1][0]) in lines:
                continue

            if slope == float("inf"):
                lines[(slope, i[1][0])] = 0
            elif slope == 0:
                lines[(0, i[1][1])] = 0
            else:
                lines[(round(slope, 5), round(y_int, 5))] = 0

        for point in points:
            for line in lines:
                if line[0] == float("inf"):
                    if point[0] == line[1]:
                        lines[line] += 1
                elif line[0] == 0:
                    if point[1] == line[1]:
                        lines[line] += 1
                else:
                    if round(point[1], 2) == round(line[0] * point[0] + line[1], 2):
                        lines[line] += 1

                max_points = max(max_points, lines[line])

        return max_points
