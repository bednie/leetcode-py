from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(amount: int) -> int:
            for coin in coins[::-1]:
                memo[amount] = min(memo[amount], memo[amount - coin] + 1)

        memo = [float("inf")] * (amount + 1)
        memo[0] = 0

        for i in range(1, amount + 1):
            dp(i)

        if memo[-1] != float("inf"):
            return memo[-1]

        return -1
