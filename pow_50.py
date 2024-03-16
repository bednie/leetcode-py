class Solution:
    def myPow(self, x: float, n: int) -> float:
        match n:
            # base cases
            case 1:
                return x

            case 0:
                return 1

            # negative exponent
            case n if n < 0:
                return 1 / self.myPow(x, -n)

            # n is even
            case n if (n % 2) == 0:
                return self.myPow(x * x, n // 2)

            # n is odd
            case n if (n % 2) == 1:
                return x * self.myPow(x, n - 1)


solution = Solution()
print(solution.myPow(2.1, 3))
print(solution.myPow(2, 10))
print(solution.myPow(2, -2))
print(solution.myPow(0.00001, 2147483647))
