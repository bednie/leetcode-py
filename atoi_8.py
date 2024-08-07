class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1 
        result = 0
        
        # step 1
        s = s.strip()

        if not s:
            return 0

        # step 2
        if len(s) >= 2:
            if s[:2] == '-+' or s[:2] == '+-':
                return 0

        if s[0] == '-':
            sign *= -1
            s = s[1:]

        if not s:
            return 0

        if s[0] == '+':
            s = s[1:]

        if not s: 
            return 0

        # step 3
        for i in s:
            if i.isdigit():
                result *= 10
                result += int(i)

            else:
                break

        result = result * sign

        if result < -2**31:
            return -2**31

        if result > (2**31 - 1):
            return 2**31 - 1

        return result