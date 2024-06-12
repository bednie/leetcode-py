class Solution:
    def mySqrt(self, x: int) -> int:
        def helper(high: int, low: int, x: int) -> int:
            if x == 0:
                return 0

            mid = (high + low) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            if mid * mid < x:
                return helper(high, mid + 1, x)
            if mid * mid > x:
                return helper(mid - 1, low, x)

        return helper(x, 0, x)
