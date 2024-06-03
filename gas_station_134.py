from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left, right, tank = 0, 0, 0
        for i in range(len(gas)):
            if right < 0:
                left = i
                right = 0
            tank += gas[i] - cost[i]
            right += gas[i] - cost[i]

        if tank < 0:
            return -1
        return left
