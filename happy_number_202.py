class Solution:
    def isHappy(self, n: int) -> bool:
        nn = n
        m = 0 # sum of squares
        while nn > 0:
            d = nn % 10
            m += d * d
            nn //= 10

        if m == 1:
            return True
        
        elif m == 4 or m == n:
            return False

        else:
            return self.isHappy(m)