class Solution:
    def reverse(self, x: int) -> int:
        
        reversed = 0

        if x >= 0:
            reversed = int(str(x)[::-1])

        else: 
            reversed = -1*int(str(abs(x))[::-1])
        
        if reversed < (-2**31) or reversed > ((2**31)-1):
            return 0
            
        return reversed