from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        def jump(point: int, current_lane: int):
            lane = lanes - {current_lane}
            if obstacles[point] != 0:
                lane -= {obstacles[point]}
            elif obstacles[point] == 0:
                for i in obstacles[point + 2 : point + 50]:
                    if i != 0 and i != current_lane:
                        lane -= {i}
                        break
            return list(lane).pop()

        lanes = {1, 2, 3}
        current_lane = 2
        jumps = 0
        point = 0

        while point < len(obstacles) - 1:
            if obstacles[point + 1] == current_lane:
                current_lane = jump(point, current_lane)
                jumps += 1
            point += 1
        return jumps
