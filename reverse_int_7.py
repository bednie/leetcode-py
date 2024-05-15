class Solution:
    def reverse(self, x: int) -> int:
        maximum =  2_147_483_647
        minimum = -2_147_483_648

        if x < 0:
            x = str(x)
            x = "-" + x[:0:-1]
        else:
            x = str(x) 
            x = x[::-1]
        
        x = int(x)
        
        if x <= minimum or x >= maximum:
            return 0

        return x


sol = Solution()
assert sol.reverse(1563847412) == 0, "Something went wrong!"
