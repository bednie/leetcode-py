# 12. Integer to Roman

# Chose this to experiment with recursion, 
# mod (even though I didn't end up using mod),
# and floor division.

class Solution:
    def intToRoman(self, num: int) -> str:

        def recur(num: int, divisor: int, answer: str, map: dict) -> str:
            # base case
            if num == 0:
                return answer
            
            answer += map[divisor][num//divisor]
    
            return recur((num-(num//divisor)*divisor),(divisor//10),answer,map)

        # empty string for our answer
        roman = ""

        # we know the max input will not exceed 3999
        divisor = 1000

        # map roman numerals to dictionary values 
        romans = {1:['','I','II','III','IV','V','VI','VII','VIII','IX'],
               10:['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC',],
               100:['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
               1000:['','M','MM','MMM',],
               }
        
        return recur(num,divisor,roman,romans)