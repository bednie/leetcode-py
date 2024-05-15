class Solution:
    def reverse(self, x: int) -> int:
        max = (2 ** 31) - 1 
        min = -(2 ** 31)
        sign = 1

        x = str(x)
        x = x[::-1]
        if x[-1] == "-":
            x = x[:-1]
            sign = -1
            
        x = int(x) * sign
        
        if x <= min or x >= max:
            return 0

        return x


sol = Solution()
x = 8463847412
print(x, sol.reverse(x))
